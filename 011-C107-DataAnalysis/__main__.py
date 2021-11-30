# 011-C107-DataAnalysis
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import pandas as pd
import plotly.express as px

df = pd.read_csv('011-C107-DataAnalysis/csv/data.csv')
mean_attempts = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
plot = px.scatter(mean_attempts, x="student_id", y="level", color="attempt", size = "attempt")
plot.write_html('011-C107-DataAnalysis/index.html', auto_open=True)
