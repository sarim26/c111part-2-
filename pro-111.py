
import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    data_set = []

    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean


def plot_graph(mean_list):
    df = mean_list

    mean = statistics.mean(mean_list)

    fig = ff.create_distplot([df], ["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
    fig.show() 

    print("Sampling mean: ", mean)

    population_mean = statistics.mean(data)
    print("Population Mean",population_mean) 

mean_list = []
def setup():
    
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    plot_graph(mean_list)

setup()

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)


first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of Reading Time"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample1)/std_deviation
print("The z score is = ",z_score)