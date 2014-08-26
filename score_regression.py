#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from bokeh.plotting import *


data = pd.DataFrame.from_csv('scores.csv', header=0)
x = data['order']
y = data['score']
regression = np.polyfit(x, y, 1)

# generate actual values for the regression line
r_x, r_y = zip(*((i, i * regression[0] + regression[1]) for i in range(15)))
output_file('score_regression.html')
line(r_x, r_y, color='red')
hold(True)
scatter(x, y, marker='square', color='blue')


# TODO: This should be getting dynamically generated based on a few factors
#           - streaks ( winning streak == make larger, losing streak == make smaller )
difficulty = 1.2
next = len(data) + 1
y_prediction = next * regression[0] * difficulty + regression[1]
scatter(next, y_prediction, marker='square', color='green')
