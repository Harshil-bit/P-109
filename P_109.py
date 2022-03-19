import csv
import statistics
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv('StudentsPerformance.csv')
data=df["reading score"].tolist()
mean=statistics.mean(data)
mode=statistics.mode(data)
median=statistics.median(data)
std_deviation=statistics.stdev(data)
print("The mean is ",mean)
print("The median is ",median)
print("The mode is ",mode)
print("The standard derivation is ",std_deviation)


fig=ff.create_distplot([data],["Result"],show_hist=False)
fig.show()


first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="Std. deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Std. deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="Std. deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="Std. deviation 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="Std. deviation 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="Std. deviation 3"))

list_of_data_within_1_std_deviation=[result for result in data if result>first_std_deviation_start and result<first_std_deviation_end]
print("% of data lies within one std. deviation ",(len(list_of_data_within_1_std_deviation)*100)/len(data))
list_of_data_within_2_std_deviation=[result for result in data if result>second_std_deviation_start and result<second_std_deviation_end]
print("% of data lies within two std. deviation ",(len(list_of_data_within_2_std_deviation)*100)/len(data))
list_of_data_within_3_std_deviation=[result for result in data if result>third_std_deviation_start and result<third_std_deviation_end]
print("% of data lies within 3 std. deviation ",(len(list_of_data_within_3_std_deviation)*100)/len(data))
