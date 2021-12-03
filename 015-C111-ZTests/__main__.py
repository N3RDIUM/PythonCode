# 015-C111-ZTests
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

from os import name
from numpy.testing._private.utils import measure
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv('014-C110-SamplingDistribution/csv/data.csv')
marks = df['responses'].tolist()

marks.pop(0)

df_intervention = pd.read_csv('015-C111-ZTests/csv/data.csv')
marks_intervention = df_intervention['responses'].tolist()

marks_intervention.pop(0)

for i in marks_intervention:
    try:
        marks_intervention[marks_intervention.index(i)] = int(i)
    except ValueError:
        marks_intervention[marks_intervention.index(i)] = 0

for i in marks:
    try:
        marks[marks.index(i)] = int(i)
    except ValueError:
        marks[marks.index(i)] = 0

def random_indexes_mean(counter):
    indexes = []
    for i in range(counter):
        indexes.append(marks_intervention[random.randint(0, len(marks_intervention)-1)])
    return statistics.mean(indexes)

def main():
    _data = []
    for i in range(0, 1000):
        _data.append(random_indexes_mean(500))

    mean = statistics.mean(marks)
    mean_intervention = statistics.mean(_data)

    first_std = mean + statistics.stdev(_data)
    second_std = mean + 2 * statistics.stdev(_data)
    third_std = mean + 3 * statistics.stdev(_data)

    first_std_end = -first_std
    second_std_end = -second_std
    third_std_end = -third_std

    print('The mean is:', mean)
    print(f'The first standard deviation is {first_std}')
    print(f'The second standard deviation is {second_std}')
    print(f'The third standard deviation is {third_std}')

    z_score = (mean_intervention - mean) / statistics.stdev(marks_intervention)
    print(f'The z-score is {z_score}')

    plot = ff.create_distplot([_data], ['Marks'], show_hist=False)
    plot.add_traces(go.Scatter(x=[first_std, first_std], y=[0, 0.7], mode='lines', name='First Standard Deviation'))
    plot.add_traces(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.7], mode='lines', name='First Standard Deviation End'))
    plot.add_traces(go.Scatter(x=[second_std, second_std], y=[0, 0.7], mode='lines', name='Second Standard Deviation'))
    plot.add_traces(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.7], mode='lines', name='Second Standard Deviation End'))
    plot.add_traces(go.Scatter(x=[third_std, third_std], y=[0, 0.7], mode='lines', name='Third Standard Deviation'))
    plot.add_traces(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.7], mode='lines', name='Third Standard Deviation End'))
    plot.write_html('015-C111-ZTests/index.html', auto_open = True)

    if mean < mean_intervention:
        print('Intervention successful!')
    else:
        print('Intervention failed!')

if __name__ == '__main__':
    main()
