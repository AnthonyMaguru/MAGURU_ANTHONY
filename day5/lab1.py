#import pandas as pd

#data = {
#    "Name": ["John", "Mary", "Peter"],
#    "Age": [20, 22, 21],
#    "Course": ["Statistics", "Computer Science", "Mathematics"]
#}

#df = pd.DataFrame(data)

#print(df)

import pandas as pd

data = [
    ["John", 20, "Statistics"],
    ["Mary", 22, "Computer Science"],
    ["Peter", 21, "Mathematics"]
]

df = pd.DataFrame(data, columns=["Name", "Age", "Course"])

print(df)

print(df["Name"])