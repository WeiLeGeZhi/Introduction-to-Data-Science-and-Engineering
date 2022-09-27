#遍历练习：写⼀个Python程序，输出1-100中所有奇数，并求这些50以内奇数的乘积。
import os # 修改工作目录
import numpy as np
import pandas as pd
import scipy.stats as stats # 统计函数
import matplotlib.pyplot as plt
from plotnine import * # ggplot 绘图
from plotnine.data import mpg
from jupyterquiz import display_quiz # Quiz
ans = 1
for i in range(1,101):
    if i%2!=0:
        print(i)
        if i<50:
            ans = ans *i
print(ans)
