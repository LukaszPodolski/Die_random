import pygal
from die_class import Die

die_1 = Die(10)
die_2 = Die(10)

results = []
for i in range(1000):   #generuje 1000 żutów kościa do gry
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

frequencies = [] # zliczam wyniki do listy
max_result = die_1.num_inside + die_2.num_inside
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
print(len(frequencies))
his=list(range(min(results), max(results)+1))
print(his)
hist = pygal.Bar()
hist.force_uri_protocol = 'http'
hist.title = "Wynik rzucania pojedynczą kością D6 tysiąc razy."
hist.x_labels = his
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')