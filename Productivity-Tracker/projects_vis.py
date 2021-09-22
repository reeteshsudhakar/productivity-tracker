import plotly.graph_objs as go
import pandas as pd
from app import * 
from notion_api import *

def setupProjectsDf(projects_data,dates):
    df = pd.DataFrame(projects_data)
    df["date"] = dates
    
    return df


def projects_pie_chart(df):
    projectsTracker = [df[p].sum() for p in df.columns if p!="date"]
    labels = [p for p in df.columns if p!="date"]
        
    fig = go.Figure(data=[go.Pie(labels=labels, values=projectsTracker)])
    fig.update_layout(title="Habit Tracker")

    return fig

df = setupProjectsDf(projects_data, dates)
fig = projects_pie_chart(df)
fig.show()

def projects_scatter_plot(df):
    colormap = {}
    colorsChart = []
    colors = list(range(len(df.columns)))
    for i,w in enumerate(df.columns):
        colormap[w] = colors[i]
    
    colorsChart = [colormap[p] for p in df.columns if p!="date"]
    
    projects = [p for p in df.columns if p!="date"]
    
    fig = go.Figure(data=[go.Scatter(x=df["date"], y=df[p],mode="markers",name=p) for p in df.columns if p!="date"])
    fig.update_layout(yaxis=dict(tickvals=[df[df[p]>0][p].iloc[0] for p in df.columns if p!="date"], ticktext = [p for p in df.columns if p!="date"]),
                     title="Habit Tracker")
    fig.update_yaxes(rangemode="nonnegative")
    
    return fig

i=1
for p in df.columns:
    if p!="date" and p!="Name":
        df[p] = df[p].apply(lambda x: i if x==True else -0.5)
        i+=1


fig.show()