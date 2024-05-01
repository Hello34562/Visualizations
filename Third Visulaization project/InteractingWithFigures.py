import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('PART2/netflix_titles.csv')

# Sample 50% of the data points
df_sampled = df.sample(frac=0.5, random_state=42)

# Create a scatter plot with the sampled data points
fig = make_subplots(rows=1, cols=1)

# Plot sampled data points
fig.add_trace(go.Scatter(
    x=df_sampled['release_year'],
    y=df_sampled['duration'],
    mode='markers',
    marker=dict(color='blue'),
    name='Sampled Data',
    text=df_sampled['title'],  # Text to display on hover
    hovertemplate='Netflix Title: %{text}<br>Release Year: %{x}<br>Duration: %{y} minutes<br>',
))

# Set layout options
fig.update_layout(
    title='Netflix Titles: Release Year vs Duration',
    xaxis_title='Release Year',
    yaxis_title='Duration',
    showlegend=True
)

# Show the plot
fig.show()