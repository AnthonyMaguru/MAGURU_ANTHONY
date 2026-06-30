#They are inbuilt

import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
print(array1)

#np.zeros() - creates an array filled with zeros
array2 = np.zeros((3, 4))  # creates a 3x4
print(array2)

#random function - generates random numbers
random_array = np.random.rand(2, 3)  # creates a 2x3 array with random numbers between 0 and 1
print(random_array)

#Mathematical and statistical Functions
array5 = np.array([30,50,10])
total = np.sum(array5)
print(total)