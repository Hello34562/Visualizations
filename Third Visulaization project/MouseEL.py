import pandas as pd
import matplotlib.pyplot as plt

# Read the Netflix data from the CSV file
netflix_data = pd.read_csv('/Users/nakshatrareddy/Downloads/Spring sem/IV/Interaction Project/PART2/netflix_titles.csv')

# Assuming 'duration' for movies is formatted as 'XX min', we'll filter out movies and convert durations
movies_data = netflix_data[netflix_data['type'] == 'Movie']
movies_data['duration'] = movies_data['duration'].str.extract('(\d+)').astype(float)  # Extracting numeric part and converting to float

def enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()

fig, axs = plt.subplots(2, figsize=(10, 8))
fig.suptitle('Mouse hover over figure or axes to trigger events')

fig.canvas.mpl_connect('figure_enter_event', enter_figure)
fig.canvas.mpl_connect('figure_leave_event', leave_figure)
fig.canvas.mpl_connect('axes_enter_event', enter_axes)
fig.canvas.mpl_connect('axes_leave_event', leave_axes)

# Plotting the Netflix dataset
axs[0].plot(netflix_data['release_year'], label='Release Year')
axs[1].plot(movies_data['duration'], label='Duration')

for ax in axs:
    ax.legend()

plt.show()
