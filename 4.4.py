# 字符串练习2: 写⼀个Python程序，输⼊⼀个字符串S，去掉其中所有空格后输出。
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
for i in range(0,len(a)):
    if a[i]!=" ":
        b.append(a[i])
str = ''.join(b)
print(str)