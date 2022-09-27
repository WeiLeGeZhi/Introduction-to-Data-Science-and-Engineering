# 结合本周理论课所学内容，使⽤三种⽅法求根号2的近似值
import os  # 修改工作目录
import numpy as np
import pandas as pd
import scipy.stats as stats  # 统计函数
import matplotlib.pyplot as plt
from plotnine import *  # ggplot 绘图
from plotnine.data import mpg
from jupyterquiz import display_quiz  # Quiz
import random
import math
# 方法1
def Square_root_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if (j**2>c and g==0):
            g=j-1
        while (abs(g**2-c)>0.0001):
            g+=0.00001
            i=i+1;
            print("%d:g = %.5f" % (i,g))
Square_root_1()
# 方法2
def Square_root_2():
    i=0
    c=2
    m_max = c
    m_min = 0
    g=(m_max+m_min)/2
    while(abs(g**2-c)>0.00000001):
        if (g*g<c):
            m_min = g
        else:
            m_max = g
        g = (m_max + m_min) / 2
        i=i+1
        print("%d:g = %.13f"%(i,g))
Square_root_2()
# 方法3
def Square_root_3():
    c = 2
    g = c/2
    i=0
    while(abs(g**2-c)>0.00000000001):
        g = (g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
Square_root_3()