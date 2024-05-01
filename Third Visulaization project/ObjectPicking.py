import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
netflix_data = pd.read_csv('/Users/nakshatrareddy/Downloads/Spring sem/IV/Interaction Project/PART2/netflix_titles.csv')

# Compute the frequency of titles released per year
release_frequency = netflix_data['release_year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.set_title('Click on points to see the number of titles released per year')

line, = ax.plot(release_frequency.index, release_frequency.values, 'o', picker=True, pickradius=5)

def onpick(event):
    ind = event.ind[0]  # Get the index of the clicked point
    year = release_frequency.index[ind]
    count = release_frequency.values[ind]
    print(f'Year: {year}, Number of Titles: {count}')

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()