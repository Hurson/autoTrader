from WindPy import *
import Global

start_time = Global.start_time_1606
end_time = Global.end_time_1606
window_size = Global.WINDOW_SIZE
top = Global.TOP
bot = Global.BOT
beta = Global.BETA

def wsiTF_T():

    print start_time,'\n',end_time,'\n',top,'\n',bot,'\n',beta
    print '\n Step1: Global Imported!'
    w_TF1606 = w.wsi("TF1606.CFE","close",start_time,end_time,"BarSize = 1;Fill= Previous")
    w_T1606 = w.wsi("T1606.CFE","close",start_time,end_time,"BarSize = 1;Fill= Previous")
    w_rtd_1606 = w.wsq("TF1606.CFE,T1606.CFE","rt_latest")
    print '\n Step2: Data Initiated!'
    print '\n Step3: Data Validity Check'
    print 'The length of data 1606: ',len(w_T1606.Times)
    print 'Matched Dates? ',w_T1606.Times == w_TF1606.Times
    rtd_benchmark = beta*w_rtd_1606.Data[0][0] - w_rtd_1606.Data[0][1]
    print '\n TF-T Spread Opens in '+str(rtd_benchmark)+'!'