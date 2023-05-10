import matplotlib.pyplot as plt
import numpy as np
from die import Die
plt.style.use('_mpl-gallery')

#Create a D6
die = Die()

#Make rolls, and store results in a list
results =[]
for roll in range(1000):
    result = die.roll()
    results.append(result)

#Analize the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
fig, ax = plt.subplots()

x_values = list(range(1, die.num_sides+1))
ax.bar(x_values, frequencies, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(1, die.num_sides+1), xticks=np.arange(1, die.num_sides+1),
       ylim=(0, 167), yticks=np.arange(1,167))

plt.show()
