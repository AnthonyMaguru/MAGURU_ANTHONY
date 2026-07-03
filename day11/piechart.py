# a pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area), is proportional to the quantity it represents. While it is named for its resemblance to a pie which has been sliced, there are variations on the way it can be presented.

import matplotlib.pyplot as plt

# Data
labels = ["Apple", "Banana", "Orange", "Mango"]
sizes = [30, 25, 20, 25]

# Create pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Favorite Fruits")

plt.show()