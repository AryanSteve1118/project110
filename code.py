import plotly.figure_factory as puf
import statistics as st
import pandas as pd
import csv
import random
import plotly.graph_objects as go

garch=pd.read_csv("medium_data.csv")
data=garch["reading_time"].tolist()
# print(data)
population_mean=st.mean(data)
population_sd=st.stdev(data)
print("population_sd ",population_sd)
# karch=puf.create_distplot([data],["zarude"],show_hist=False)
# karch.show()

no_of_samples=30
len_sample=100
def get_sample():
    sam1=[]
    for i in range(0,len_sample):
        sample1=random.randint(0,len(data))
        value=data[sample1]
        sam1.append(value)
    # print(sam1)
    mean=st.mean(sam1)
    # std=st.stdev(sam1)
    return mean

def get_mean_list():
    mean_list=[]
    for i in range(0,no_of_samples):
        mean1=get_sample()
        mean_list.append(mean1)
    # print(mean_list)
    return mean_list

def setup():
    m_l=get_mean_list()
    mean1=st.mean(m_l)
    sd = st.stdev(m_l)
    print("sampling_sd: ",sd)
    karch=puf.create_distplot([m_l],["zarude"],show_hist=False)
    karch.add_trace(go.Scatter(x=[mean1,mean1],y=[0,1],mode="lines",name="mean"))
    karch.show()

setup()
