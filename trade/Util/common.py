# coding utf-8
import time


# 用户账户密码信息
userId = 'M:1875511385902'
userPassCode = '489726'




# 设置默认价差计算参数
WINDOW_SIZE = 1500
TOP = 1.28
BOT = -1.28
BETA = 1.65
CUT_LOST = -0.1
GAIN_PROFIT = 0.1

# Wind数据在主程序里面打开，因为主程序要连接上WindPy才能不断地刷新数据
start_time_1606 = "2016-02-03" # 1606合约活跃起始期
end_time_1606 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))