"""Ten nie działa """

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die_class import Die
#import plotly.graph_objs as go

die = Die()
results = []
for i in range(1000):   #generuje 1000 żutów kościa do gry
    result = die.roll()
    results.append(result)
print(results)
frequencies = []
for value in range(1, die.num_inside+1): # zliczam wyniki
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

x_values = [1,range(1,die.num_inside+1)]
data = [Bar(x = x_values, y = frequencies)]
x_axis = {'title': 'Results'}
y_axis = {'title': 'frequency of occurrence of values '}
my_layout = Layout(title = "jghjhgjjhgjh", xaxis=x_axis, yaxis= y_axis)
offline.plot(({'data': data, 'layout': my_layout}),filename= 'd6.html')
