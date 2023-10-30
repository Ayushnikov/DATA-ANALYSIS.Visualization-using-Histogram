import matplotlib.pyplot as plt
import pandas as pd


# You can load it into a pandas DataFrame like this:
df = pd.read_csv("iris.csv")

# Get the list of all columns in the DataFrame
columns = df.columns
# Set the number of subplots based on the number of columns
num_plots = len(columns)

# Create subplots
fig, axs = plt.subplots(nrows=num_plots, ncols=1, figsize=(8, 2 * num_plots))

# Iterate through each column and create a histogram or bar chart
for i, column in enumerate(columns):
    axs[i].hist(df[column], bins=20, color='lightblue', edgecolor='black')
    axs[i].set_xlabel(column)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title(f'Histogram of {column}')

# Adjust layout to prevent overlapping
plt.tight_layout()

plt.show()