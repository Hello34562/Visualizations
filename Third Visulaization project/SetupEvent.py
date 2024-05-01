#Setup of event for a project
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load the Netflix dataset
netflix_data = pd.read_csv('/Users/nakshatrareddy/Downloads/Spring sem/IV/Interaction Project/PART2/netflix_titles.csv')

# Function to handle button click event
def show_random_title():
    # Select a random row from the dataset
    random_row = netflix_data.sample(1)
    # Display title information in a message box
    messagebox.showinfo("Random Netflix Title", f"Title: {random_row['title'].values[0]}\nType: {random_row['type'].values[0]}\nRelease Year: {random_row['release_year'].values[0]}")

# Create the main application window
root = tk.Tk()
root.title("Random Netflix Title Viewer")

# Create a label widget
label = tk.Label(root, text="Click the button to view a random Netflix title!")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Show Random Title", command=show_random_title)
button.pack()

# Run the application
root.mainloop()

