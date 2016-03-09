# coding:utf-8
from numpy import *
def Normal_Linear_Method(input_data,window_size):
# 之后可以先check数据有效性
    output_data_N = []
    total_number = len(input_data)
    for i in range(window_size,total_number):
        max_data = max(input_data[i-window_size:i])
        min_data = min(input_data[i-window_size:i])
        temp = true_divide((input_data[i]-min_data),(max_data-min_data))
        output_data_N.append(temp)
    return output_data_N


def Normal_Zscore_Metho(input_data,window_size):
    output_data_N = []
    total_number = len(input_data)
    for i in range(window_size,total_number):
        mean_data = mean(input_data[i-window_size:i])
        std_data = std(input_data[i-window_size:i])
        temp = true_divide((input_data[i]-mean_data),std_data)
        output_data_N.append(temp)
    return output_data_N


# unNormal
def unNormal_Linear_Method(input_data_unN,window_size,critical_value):
    output_data_unN = []
    total_number = len(input_data_unN)
    for i in range(window_size,total_number):
        max_data = max(input_data_unN[i-window_size:i])
        min_data = min(input_data_unN[i-window_size:i])
        temp = critical_value*(max_data-min_data)+min_data
        output_data_unN.append(temp)
    return output_data_unN

def unNormal_Zscore_Method(input_data_unN,window_size,critical_value):
    output_data_unN = []
    total_number = len(input_data_unN)
    for i in range(window_size,total_number):
        mean_data = mean(input_data_unN[i-window_size:i])
        std_data = std(input_data_unN[i-window_size:i])
        temp = critical_value*std_data+mean_data
        output_data_unN.append(temp)
    return output_data_unN
