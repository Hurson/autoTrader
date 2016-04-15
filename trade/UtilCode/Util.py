# coding:utf-8

from WindPy import *
from Tkinter import *
from tkMessageBox import *


#启动windpy
def startWindPy():
    w.start()

    if w.isconnected():
        print '\n WindPy Started!'
    else:
        showwarning('登录失败','启动winpy失败')
        sys.exit()

#登录交易账号
def login():
    Login_Info = w.tlogon("00000010","0","M:1875511385902","******","CFE")
    if Login_Info.ErrorCode == 0:
        print('登录资金账户成功')
        print Login_Info
        return Login_Info.Data[0][0]
    else:
        showwarning('登录失败','登录资金账户异常')
        sys.exit()

#查询对应商品的持仓信息
#{登录ID，产品名称}
#return [成本，方向，仓位，当前价位]
def queryPosition(loginId,SecurityName):
    positionInfo = w.tquery("Position","LogonId="+loginId)
    try:
        i = positionInfo.Data[1].index(SecurityName)
        flag = None
        if "Buy" in positionInfo.Data[4][i]:
            flag = 1
        elif "Short" in positionInfo.Data[4][i]:
            flag = -1
        Position = [positionInfo.Data[2][i],flag,positionInfo.Data[6][i],positionInfo.Data[3][i]]
        return Position
    except:
        ValueError
        showwarning('查询失败','查询持仓信息异常')
        print positionInfo
        sys.exit()

##下单委托
##(交易代码，交易类型，委托价格，下单手数，登录编号)
def torder(SecurityCode,TradeSide,OrderPrice,OrderVolume,LogonID):
    w.torder(SecurityCode,TradeSide,OrderPrice,OrderVolume,"OrderType=LMT;"+LogonID)
##根据下单时requestId查询委托信息

    ##（登录编号，请求编号）
def queryOrder(loginId,requestId):
    arg1 = "LogonId="+loginId;
    arg2 = ";RequestID="+requestId;
    orderInfo = w.tquery("Order",arg1+arg2)
    return orderInfo

##撤单委托
##（登录编号，委托编号）
def tcancel(logonId,orderId):
    cancelInfo = w.tcancel(orderId,"LogonID="+logonId)
    print cancelInfo
    if cancelInfo.Data[2][0] == 0 :
        print "撤销委托成功"
        return cancelInfo
    else:
        print "撤销委托失败！"

##查询卖一买一价
##[卖一][买一]
def askBid():
    rt = w.wsq("TF1606.CFE,T1606.CFE", "rt_ask1,rt_bid1").Data
    return rt

if __name__ == '__main__':
    startWindPy()
    login()
    print w.tquery("Position","LogonId=1")
    print queryPosition("1","T1606")

