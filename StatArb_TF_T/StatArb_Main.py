# coding:utf-8
# 交易的时候，要程序找到价差合理的位置成交，但是这涉及到两个循环嵌套的问题。
# 未来把策略判断部分封装一下

from numpy import *
from WindPy import *


import Global
import Normal

# 链接WindPy
w.start()
w.isconnected()
print '\n WindPy Started!'

# 登陆交易账号
Login_Info = w.tlogon("00000010","0","M:1875511385902","******","CFE")
print Login_Info
# 添加交易登陆失败并进行相关弹窗显示原因并且中断程序

# 第一步：导入初始状态数据（开盘或者开始运行程序时） - 这部分参数从程序开始就不会改变。
start_time = Global.start_time_1606
end_time = Global.end_time_1606
window_size = Global.WINDOW_SIZE
top = Global.TOP
bot = Global.BOT
beta = Global.BETA
print start_time,'\n',end_time,'\n',top,'\n',bot,'\n',beta
print '\n Step1: Global Imported!'

# 第二步：初始化合约历史价格情况 （把开始时间设置为end time前2倍window size的时间点）
w_TF1606 = w.wsi("TF1606.CFE","close",start_time,end_time,"BarSize = 1;Fill= Previous")
w_T1606 = w.wsi("T1606.CFE","close",start_time,end_time,"BarSize = 1;Fill= Previous")
w_rtd_1606 = w.wsq("TF1606.CFE,T1606.CFE","rt_latest")
print '\n Step2: Data Initiated!'
print '\n Step3: Data Validity Check'
print 'The length of data 1606: ',len(w_T1606.Times)
print 'Matched Dates? ',w_T1606.Times == w_TF1606.Times

rtd_benchmark = beta*w_rtd_1606.Data[0][0] - w_rtd_1606.Data[0][1]
print '\n TF-T Spread Opens in '+str(rtd_benchmark)+'!'


# 第三步：初始化策略交易位置：从交易账户中提取如下信息：1.当前仓位，2.当时开仓平均成本，3.直接判断目前开仓是否有才操作指令要求。
###tInfo = w.tquery(2)  相关指令   根据数据结构获取所需要的信息  @Hurson

flag_position = 'None'  ##仓位
flag_gp_cl = 'None'     ##止盈止损状态   高位/低位 止盈止损


# 第四步：计算实时上下阈值 (需要实时刷新)
##ASP框架定时任务 @Hurson

benchmark = 1.95*array(w_TF1606.Data[0]-w_T1606.Data[0])
uplimit_series = Normal.unNormal_Zscore_Method(benchmark,window_size,top)
botlimit_series = Normal.unNormal_Zscore_Method(benchmark,window_size,bot)
uplimit_rtd = uplimit_series[len(uplimit_series)-1]
botlimit_rtd = botlimit_series[len(botlimit_series)-1]
unRealized_PnL_rtd = 0 #根据开仓成本和仓位计算实时浮动损益




# 第五步：判断策略操作（需要实时不断判断）

    # 判断止盈止损区间
if 0.7*(uplimit_rtd-botlimit_rtd)<=0.1:
    cl = -0.7*(uplimit_rtd-botlimit_rtd)
    gp = 0.7*(uplimit_rtd-botlimit_rtd)
else:
    cl = Global.CUT_LOST
    gp = Global.GAIN_PROFIT

    # 判断策略操作点：
    # 向下做价差平+开仓：
if rtd_benchmark >= uplimit_rtd and flag_position != 'Short' and flag_gp_cl != 'Top-cut':
    # 执行short TF long T 操作 以及其余的判断操作
    flag_position = 'Short'
    flag_gp_cl = 'None'


    # 向上做价差平+开仓：
elif rtd_benchmark <= botlimit_rtd and flag_position !='Long' and flag_gp_cl != 'Bot-cut':
    # 执行long TF short T 操作 以及其余的判断操作
    flag_position = 'Long'
    flag_gp_cl = 'None'

    # 止损：
elif flag_position == 'Short' and unRealized_PnL_rtd <= cl:
    # 执行平仓操作
    flag_gp_cl = 'Top-cut'
    flag_position = 'None'

elif flag_position == 'Long' and unRealized_PnL_rtd <= cl:
    # 执行平仓操作
    flag_gp_cl = 'Bot-cut'
    flag_position = 'None'

    # 止盈
elif flag_position == 'Short' and unRealized_PnL_rtd >= gp:
    # 执行平仓操作
    flag_gp_cl = 'Up-gain'
    flag_position = 'None'

elif flag_position == 'Long' and unRealized_PnL_rtd >= gp:
    # 执行平仓操作
    flag_gp_cl = 'Bot-gain'
    flag_position = 'None'

# 循环以上部分，并计算实时数据，确认交易成交信息等。

# 数据可视化，结合IRR策略等信息。




