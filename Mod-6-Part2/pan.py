# pandas is mainly for data manipulation

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

# myCalories = pd.Series(calories)
myCalories = pd.Series(calories, index=["day1","day2"])
print(myCalories)

# a dictionary is created
myDataset = {
    'cars': ["BMW","Volvo","Ford"],
    'passing': [3,7,2]
}

df = pd.DataFrame(myDataset)
print(df)
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape) # like 3X2

data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}

dataframe = pd.DataFrame(data,index=["day1","day2","day3"])
print(dataframe)