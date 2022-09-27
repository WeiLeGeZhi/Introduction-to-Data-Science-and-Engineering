#循环练习：写⼀个Python程序，实现分别⽤for和while循环、数组切⽚实现对⼀个给定列表的倒排序输出。给定列表： l = [1,2,3,4,5]
import os # 修改工作目录
import numpy as np
import pandas as pd
import scipy.stats as stats # 统计函数
import matplotlib.pyplot as plt
from plotnine import * # ggplot 绘图
from plotnine.data import mpg
from jupyterquiz import display_quiz # Quiz
l = [1,2,3,4,5]
# for循环
for i in range(0,5):
    print(l[4-i])
# while循环
i_ = 4
while i_ >=0:
    print(l[i_])
    i_=i_-1
# 数组切片
a = l[::-1]
print(a)