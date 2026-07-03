# a simple graph that shows how data is spread out. it displays the minimum and the maximum values, the median, and the first and third quartiles of a dataset. it is useful for identifying outliers and understanding the distribution of data.
# a simple box plot

import matplotlib.pyplot as plt


#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#plt.boxplot(data)
#plt.title("Simple Box Plot")
#plt.ylabel("Values")
#plt.show()

# Sample data
math_scores = [70, 75, 80, 85, 90, 95, 88, 76]
science_scores = [65, 68, 72, 78, 82, 85, 89, 91]
english_scores = [60, 65, 70, 72, 75, 80, 85, 88]

# Create box plot
plt.boxplot([math_scores, science_scores, english_scores])

# Labels
plt.title("Students' Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks([1, 2, 3], ["Math", "Science", "English"])

plt.show()
