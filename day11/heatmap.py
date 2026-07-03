#A heat map is a chart that uses colors to represent values in a 
# matrix or table. In Python, it's commonly created using Matplotlib


"""import matplotlib.pyplot as plt
import numpy as np

# Sample data
scores = np.array([
    [80, 75, 90],
    [85, 88, 92],
    [70, 95, 85]
])

students = ["Alice", "Bob", "Carol"]
subjects = ["Math", "Science", "English"]

plt.imshow(scores, cmap="coolwarm")

# Add labels
plt.xticks(range(len(subjects)), subjects)
plt.yticks(range(len(students)), students)

# Color scale
plt.colorbar(label="Marks")

plt.title("Student Scores Heat Map")

plt.show()"""

# using seaborn library
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame
data = pd.DataFrame(
    [
        [80, 75, 90],
        [85, 88, 92],
        [70, 95, 85]
    ],
    index=["Alice", "Bob", "Carol"],
    columns=["Math", "Science", "English"]
)

sns.heatmap(
    data,
    annot=True,
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Student Marks Heat Map")
plt.show()