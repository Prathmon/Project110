import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as ss
import random

file1 = pd.read_csv("medium_data.csv")
data = file1["claps"].to_list()
population_mean = ss.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = ss.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["claps"], show_hist = False)
    fig.show()
    sampling_mean = ss.mean(df)
    print("Sampling mean = ", sampling_mean)

print("Population mean = ", population_mean)
setup()