# （选做）⾄少使⽤三种⽅法求解PI的值，并⽐较他们的效率（精度保留在⼩数点后10位）
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
N = 10000000
C = 0
for i in range(N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,1.0)
    if x**2+y**2<=1:
        C+=1
I = C/N
PI = 4*I
print(PI)