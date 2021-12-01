# 013-C109-BellCurve-2
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('013-C109-BellCurve-2/csv/students.csv')
scores = df['math score'].tolist()

mean_ = statistics.mean(scores)
median_ = statistics.median(scores)
mode_ = statistics.mode(scores)
stdev_ = statistics.stdev(scores)

print(f'Mean: {mean_}')
print(f'Median: {median_}')
print(f'Mode: {mode_}')
print(f'Standard Deviation: {stdev_}')

# get percent of values between 1st standard deviation
count = 0
for score in scores:
    if score > mean_ - stdev_ and score < mean_ + stdev_:
        count += 1
_1perc = (count / len(scores))*100
print('1st Standard Deviation:', _1perc, '%')

# get percent of values between 2nd standard deviation
count = 0
for score in scores:
    if score > mean_ - (stdev_ * 2) and score < mean_ + (stdev_ * 2):
        count += 1
_2perc = (count / len(scores))*100
print('2nd Standard Deviation:', _2perc, '%')

# get percent of values between 3rd standard deviation
count = 0
for score in scores:
    if score > mean_ - (stdev_ * 3) and score < mean_ + (stdev_ * 3):
        count += 1
_3perc = (count / len(scores))*100
print('3rd Standard Deviation:', _3perc, '%')

figure = ff.create_distplot([scores], ['Math Scores'])
figure.write_html('013-C109-BellCurve-2/index.html', auto_open=True)
