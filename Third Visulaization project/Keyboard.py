import pandas as pd
import matplotlib.pyplot as plt

# Read the Netflix data from the CSV file
netflix_data = pd.read_csv('/Users/nakshatrareddy/Downloads/Spring sem/IV/Interaction Project/PART2/netflix_titles.csv')

# Function to plot different views of the Netflix dataset
def plot_data(view):
    plt.figure(figsize=(10, 6))
    if view == 'release_year':
        plt.hist(netflix_data['release_year'], bins=30, color='skyblue', edgecolor='black')
        plt.xlabel('Release Year')

        plt.ylabel('Frequency')
        plt.title('Distribution of Netflix Titles by Release Year')
    elif view == 'duration':
        # Convert 'duration' values to string before plotting
        duration_str = netflix_data['duration'].astype(str)
        plt.hist(duration_str, bins=30, color='salmon', edgecolor='black')
        plt.xlabel('Duration')
        plt.ylabel('Frequency')
        plt.title('Distribution of Netflix Titles by Duration')
    plt.grid(True)

# Function to handle user input
def get_user_input():
    while True:
        user_input = input("Enter 'r' to view by release year, 'd' to view by duration: ")
        if user_input.lower() in ['r', 'd']:
            return user_input.lower()
        else:
            print("Invalid input. Please enter 'r' or 'd'.")

# Main loop to handle user input
while True:
    user_choice = get_user_input()
    if user_choice == 'r':
        plot_data('release_year')  # Plot by release year
        plt.show()  # Display the plot
        break  # Exit loop after plotting
    elif user_choice == 'd':
        plot_data('duration')  # Plot by duration
        plt.show()  # Display the plot
        break  # Exit loop after plotting