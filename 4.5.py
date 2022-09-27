# 蒙特卡罗求积分
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
s = 1*2
N = 1000000
C = 0
for i in range(N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,2.0)
    if y <= x**2+x**3:
        C+=1
I = C/N*s
print(I)