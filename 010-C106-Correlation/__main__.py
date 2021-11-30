# 010-C106-Correlation
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import pandas as pd
import plotly_express as px
import csv
import numpy as np
import os

def corrcoef(_,__):
    return np.corrcoef(_,__)[0,1]

def get_attrs(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

        attrs = data[0]
        return attrs

def map_dir_for_csvs(path):
    _ = []
    for i in os.listdir(path):
        if i.endswith('.csv'):
            _.append(i)
    return _

def do_corrcoef_for_dir(path):
    _ = []
    for i in map_dir_for_csvs(path):
        _.append(i)

    for i in _:
        full_path = path + '/' + i
        all_attrs = get_attrs(full_path)

        df = pd.read_csv(full_path)
        correlation = corrcoef(df[all_attrs[1]], df[all_attrs[2]])
        plot = px.scatter(df, x=all_attrs[1] ,y=all_attrs[2] , size=all_attrs[0], title="Correlation: "+str(correlation))
        plot.write_html('010-C105-Correlation/index.html', auto_open=True)

if __name__ == '__main__':
    do_corrcoef_for_dir('010-C105-Correlation/csv')
