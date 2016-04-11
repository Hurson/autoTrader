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


tick = w.wsq("T1606.CFE", "rt_ask1,rt_bid1")

ws = w.wsi("T1606.CFE", "close", "2016-03-01 09:00:00", "2016-03-08 14:52:13", "")
b = w.tlogon("00000010","0","M:1875511385902","******","CFE")

a = w.torder("TF1606.CFE","Buy",str(tick.Data[1][0]),"200","OrderType=LMT;LogonID="+str(b.Data[0][0]))
d = w.tquery("Order","LogonId=1;RequestID="+str(a.Data[0][0]))
print a
print d
time.sleep(5)
c = w.tquery("Position","LogonId=1")
d = w.tquery("Order","LogonId=1")
e = w.tquery("Trade","LogonId=1")
print b
print c
print d
print e
