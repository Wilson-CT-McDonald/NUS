import pandas as pd

file = pd.read_csv('test.csv')

print(file.to_string()) # to see a full file
# print(file) # to see partial data

""" file.options.display.max_rows = 100
new_file = file.dropna() # remove all the null records in data
df = file.dropna(inplace = True) # Remove all the null rows from the actual file """


# below is the Manali Dubai Tutorials

# total sales per department
ans = file.groupby('Department')['Sales'].sum()

# top performer (highest sales)
ans2 = df[df['Sales']==df['Sales'].max()]['Employee']
print(ans2)

# hours worked > 40
ans3 = df[df['Hours_Worked']>40]['Employee'].tolist()