# 012-C108-BellCurve
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('012-C108-BellCurve/csv/data.csv')
figure = ff.create_distplot([df['Rating'].tolist()],['Rating'], show_hist=False,)
figure.write_html('012-C108-BellCurve/index.html', auto_open=True)
