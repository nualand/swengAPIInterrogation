import plotly
import plotly.plotly as py


import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
import csv


username="nualand"
key="vss30CAgma5dqLwpdHEq"



with open('csv/repostitory_info.csv') as csvfile:
   readCSV = csv.reader(csvfile, delimiter=',')
   repo_nums = []
   repo_names = []
   repo_pulls = []
   repo_stars = []

   for row in readCSV:
       repo_num = row[0]
       repo_name = row[1]
       repo_pull = row[2]
       repo_star = row[3]

       repo_nums.append(repo_num)
       repo_names.append(repo_name)
       repo_pulls.append(repo_pulls )
       repo_stars.append(repo_star)


xs = repo_names
ys = repo_stars
zs = repo_pulls
texts = repo_names

trace0 = go.Bar(
    x= xs,
    y=ys,
        # text= texts,
    # marker=dict(
    #     color='rgb(158,202,225)',
    #
    #     )

opacity=0.6

)
#
# trace1 = go.Scatter(
#     x = xs,
#     y = zs,
#
# )
data = [trace0]
layout = go.Layout(
    title='Stars per Repo',
)
choromap = go.Figure(data = data,layout = layout)

plotly.offline.plot(choromap)
