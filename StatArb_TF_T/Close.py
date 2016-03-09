# coding:utf-8
from WindPy import *
def close_position(TPosition,TFPositon,TBuyOne,TSaleOne,TFBuyOne,TFSaleOne):
    #买平空仓
    if TPosition<0:
        w.torder("T1606.CFE","CoverToday",TBuyOne,-1*TPosition,"OrderType=LMT")
    elif TPosition>0: #卖平多仓
        w.torder("T1606.CFE","SellToday",TSaleOne,TPosition,"OrderType=LMT")

    if TFPositon<0:
        w.torder("TF1606.CFE","CoverToday",TFBuyOne,-1*TFPositon,"OrderType=LMT")
    elif TFPositon>0: #卖平多仓
        w.torder("TF1606.CFE","SellToday",TFSaleOne,TFPositon,"OrderType=LMT")
    print("执行平仓指令")