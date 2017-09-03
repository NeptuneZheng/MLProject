import numpy as np
from pylab import *
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator = MultipleLocator(10)  # 将x主刻度标签设置为10的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数

def FileReader(filepath):
    file = open(filepath)
    time = []
    Qt = []
    for line in file.readlines()[1:]:
        arr = line.strip().replace("\n","").split("\t")
        if(arr.__len__()>1):
            time.append(float(arr[0]))
            Qt.append(float(arr[1]))


    fitting1 = np.polyfit(time,Qt,2)
    fitObj1 = np.poly1d(fitting1)
    print(fitObj1)

    popt, pcon = curve_fit(fun,time,Qt)
    a = popt[2]
    b = popt[3]
    yvals = fun(time,a,b)
    ax = subplot(111)
    # print origing data in dashboard
    plt.plot(time, Qt, 'yo',marker='d',label='Orignal Data Point')
    # print fitting line
    plt.plot(time,fitObj1(time),'r',label='Predict Line By Data')
    plt.plot(time,yvals,'p',label='Predict Line By Math')
    # plt.plot(time,Qt,'b',linewidth=1)
    plt.legend(loc = 4)

    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)

    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)

    # 显示次刻度标签的位置,没有标签文本
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)

    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    # ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.show()

def fun(x,a,b):
    return a-math.exp(math.log(math.e,a)-x)

FileReader("../source/source.txt")