import pandas as pd

file = pd.read_csv('test.csv')

print(file.to_string()) # to see a full file
print(file) # to see partial data

file.options.display.max_rows = 100
new_file = file.dropna() # remove all the null records in data
df = file.dropna(inplace = True) # Remove all the null rows from the actual file

print(df.to_string())