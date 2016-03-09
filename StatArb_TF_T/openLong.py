#coding = utf-8# coding:utf-8

from WindPy import *
import StatArb_Main as s

def openLong(TTargetPosition,TFTargetPosition,,TFSaleOne,TBuyOne):
    TFLongInfo = w.torder("TF1606.CFE","Buy","102","3","OrderType=LMT")
    #判断委托是否成功
    if TFLongInfo.ErrorCode != '0':
        #委托成功，开始循环判断订单交易状态  在一定时间内有没有成交
            #true ：开始下一步操作
            #false ： 撤单操作。
