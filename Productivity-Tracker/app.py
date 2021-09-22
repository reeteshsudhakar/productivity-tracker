import streamlit as st
import seaborn as sns
sns.set()
from projects_vis import *
from notion_api import *


# Caches automatically
@st.cache
def load_data():
    nsync = NotionSync()
    data = nsync.query_databases()
    projects = nsync.get_projects_titles(data)
    projects_data,dates = nsync.get_projects_data(data,projects)
    df = setupProjectsDf(projects_data,dates)
    return df

    

df = load_data()
i=1
for p in df.columns:
    if p!="date" and p!="Name":
        df[p] = df[p].apply(lambda x: i if x==True else -0.5)
        i+=1


st.title("Habit Tracker")

# Set up: load and set up the data and write loading message
data_load_state = st.text('Loading data...')
data_load_state.text('Loading data...done!')

# Plotting Projects Stats
st.subheader("Habit Tracker")
project_time_spents = projects_pie_chart(df)
st.write(project_time_spents)
project_events = projects_scatter_plot(df)
st.write(project_events)