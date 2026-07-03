# A scatter plot is a type of plot that displays values for typically two variables for a set of data. The data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.
# Scatter plots are used to observe relationships between variables. They can show how much one variable is

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 7, 6, 8]

# Create scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title("Simple Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()