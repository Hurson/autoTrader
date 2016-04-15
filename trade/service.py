# coding:utf-8
##中层引擎，组合业务逻辑

from WindPy import *
from Tkinter import *
from tkMessageBox import *
from UtilCode import common as c
from UtilCode import Util as u
from UtilCode import Normal
from numpy import *


##初始化合约历史价格情况
def initHis(startTime,endTime,beta):
    w_TF1606 = w.wsi("TF1606.CFE","close",startTime,endTime,"BarSize = 1;Fill= Previous")
    w_T1606 = w.wsi("T1606.CFE","close",startTime,endTime,"BarSize = 1;Fill= Previous")
    w_rtd_1606 = w.wsq("TF1606.CFE,T1606.CFE","rt_latest")
    print '\n Step2: Data Initiated!'
    print '\n Step3: Data Validity Check'
    print 'The length of data 1606: ',len(w_T1606.Times)
    print 'Matched Dates? ',w_T1606.Times == w_TF1606.Times

    rtd_benchmark = beta*w_rtd_1606.Data[0][0] - w_rtd_1606.Data[0][1]
    print '\n TF-T Spread Opens in '+str(rtd_benchmark)+'!'
    return [w_TF1606,w_T1606,w_rtd_1606,rtd_benchmark]

##初始化交易策略位置
def initStrategy(loginId):
    ##查询仓位
    TPsition = u.queryPosition(loginId,"T1606")
    TFPsiton = u.queryPosition(loginId,"TF1606")
    return [TPsition,TFPsiton]

##计算实时上下阈值
def threshold(w_TF1606,w_T1606):
    benchmark = c.BETA*array(w_TF1606.Data[0]-w_T1606.Data[0])
    uplimit_series = Normal.unNormal_Zscore_Method(benchmark,c.WINDOW_SIZE,c.TOP)
    botlimit_series = Normal.unNormal_Zscore_Method(benchmark,c.WINDOW_SIZE,c.BOT)
    uplimit_rtd = uplimit_series[len(uplimit_series)-1]
    botlimit_rtd = botlimit_series[len(botlimit_series)-1]
    return [uplimit_rtd,botlimit_rtd]

