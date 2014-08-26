#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from bokeh.plotting import *


def simple_linear_regression(x, y):
    length = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    # ∑x^2 and ∑xy
    sum_x_squared = sum(map(lambda a: a * a, x))
    covariance = sum([x[i + 1] * y[i + 1] for i in range(length)])

    a = (covariance - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
    b = (sum_y - a * sum_x) / length
    return a, b


housing_data = pd.DataFrame.from_csv('housing.csv', header=0)
x = housing_data['area']
y = housing_data['selling price']
# regression = simple_linear_regression(x, y)
regression = np.polyfit(x, y, 1)

# generate actual values for the regression line
r_x, r_y = zip(*((i, i * regression[0] + regression[1]) for i in range(15)))
output_file('housing_regression.html')
line(r_x, r_y, color='red')

# Specify that the two graphs should be on the same plot.
hold(True)
scatter(x, y, marker='square', color='blue')
