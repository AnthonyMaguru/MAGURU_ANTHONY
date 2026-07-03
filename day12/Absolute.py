# An example of maximum scaling in python using scikit-learn library

import pandas as pd
import numpy as np

df = pd.read_csv("Housing.csv")

df = df.select_dtypes(include=np.number)

#print(df.head())



