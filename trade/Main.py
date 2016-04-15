# coding:utf-8

from numpy import *
from WindPy import *
from Tkinter import *
from tkMessageBox import *
from UtilCode import Util as u
from UtilCode import common as c
from UtilCode import Normal
import service


""""
策略实现细节
全局变量
loginID:wind登录时记录的ID，供其它wind相关操作使用
flag_gp_cl：止盈止损标记位
"""""


##启动windpy
u.startWindPy()

##登录交易账号,记录全局变量loginId
loginID = u.login()

##初始化全局变量 止盈止损状态
##00：低位止损 01：低位止盈 10高位止损 11高位止盈
flag_gp_cl = "00"


## 第一步：导入初始状态数据（开盘或者开始运行程序时） - 这部分参数从程序开始就不会改变。
start_time = c.start_time_1606
end_time = c.end_time_1606
window_size = c.WINDOW_SIZE
top = c.TOP
bot = c.BOT
beta = c.BETA
print start_time,'\n',end_time,'\n',top,'\n',bot,'\n',beta
print '\n Step1: Global Imported!'


# 第二步：初始化合约历史价格情况 （把开始时间设置为end time前2倍window size的时间点）
HisInfo = service.initHis(start_time,end_time,beta)
w_TF1606 = HisInfo[0]
w_T1606 = HisInfo[1]
w_rtd_1606 = HisInfo[2]
rtd_benchmark = HisInfo[3]


# 第三步：初始化策略交易位置：从交易账户中提取如下信息：1.当前仓位，2.当时开仓平均成本，3.直接判断目前开仓是否有才操作指令要求。
StrInfo = service.initStrategy(loginID)
TPsition = StrInfo[0]
TFPsiton = StrInfo[1]

# 第四步：计算实时上下阈值 (需要实时刷新)
ths = service.threshold(w_TF1606,w_T1606)
unRealized_PnL_rtd = (TPsition[3]-TPsition[0])*TPsition[2]*TPsition[1] #根据开仓成本和仓位计算实时浮动损益\



# 第五步：判断策略操作（需要实时不断判断）
# 判断止盈止损区间
if 0.7*(ths[0]-ths[1])<=0.1:
    cl = -0.7*(ths[0]-ths[1])
    gp = 0.7*(ths[0]-ths[1])
else:
    cl = c.CUT_LOST
    gp = c.GAIN_PROFIT

    # 判断策略操作点：
    # 向下做价差平+开仓：

