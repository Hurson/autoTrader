# coding:utf-8
from WindPy import *
import time
w.start()
w.isconnected()
print '\n WindPy Started!'

Login_Info = w.tlogon("00000010","0","M:1875511385902","******","CFE")
print Login_Info

BuyInfo = w.wsq("TF1606.CFE", "rt_latest")

print BuyInfo


tick = w.wsq("TF1606.CFE", "rt_ask1,rt_bid1", func=DemoWSQCallback)
w = w.wsi("TF1606.CFE", "close", "2016-03-01 09:00:00", "2016-03-08 14:52:13", "")

while 1==1:
    print tick
    print'======================================================================='
    print len(w.Data[0])
    print'======================================================================='
    time.sleep(5)


b = w.tlogon("00000010","0","M:1875511385902","******","CFE")

a = w.torder("TF1606.CFE","Buy",BuyInfo.Data[0],"20","OrderType=LMT;LogonID="+str(b.Data[0][0]))
print b
print a