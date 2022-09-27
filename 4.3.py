# 字符串练习：写⼀个Python程序，判断⼀个输⼊的字符串s，是否包含两个或两个以上连续出现的相同字符组成的字符串，并输出最⻓连续出现的字符⻓度。
import os  # 修改工作目录
import numpy as np
import pandas as pd
import scipy.stats as stats  # 统计函数
import matplotlib.pyplot as plt
from plotnine import *  # ggplot 绘图
from plotnine.data import mpg
from jupyterquiz import display_quiz  # Quiz
a = input("请输入一个字符串:")
b = []
xtzfc = 1
for i in range(0,len(a)-1):
    if a[i] is a[i+1]:
        xtzfc=xtzfc+1
    else:
        b.append(xtzfc)
        xtzfc=1
b.sort()
print(b[len(b)-1])