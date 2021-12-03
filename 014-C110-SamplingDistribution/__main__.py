# 014-C110-SamplingDistribution
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('014-C110-SamplingDistribution/csv/data.csv')

data_list = df['responses'].tolist()

def show_figure(mean_list, mean):
    df = mean_list
    fig = ff.create_distplot([df], ['temp'], show_hist=False)
    fig.add_trace(go.Scatter(
        x=[mean, mean],
        y=[0, 1],
        mode='lines',
        name='mean',
    ))
    fig.write_html('014-C110-SamplingDistribution/index.html', auto_open=True)

def get_random_set_of_means(data_list, number_of_means):
    random_set_of_means = []
    for i in range(number_of_means):
        random_set_of_means.append(random.choice(data_list))

    return statistics.mean(random_set_of_means)

def main():
    mean_list = []
    for i in range(10000):
        mean_list.append(get_random_set_of_means(data_list, 100))
    mean = statistics.mean(mean_list)
    print(f"Standard Deviation: {statistics.stdev(mean_list)}")
    show_figure(mean_list, mean)

if __name__ == '__main__':
    main()
