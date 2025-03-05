# py -m pip install numpy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q1
# a) Create a 2D NumPy array (3x3) with float64 elements
array1 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype=np.float64)
print(array1)

# b) Element-wise addition with scalar 10
array_add = array1 + 10
print(array_add)

# c) Element-wise multiplication with another 3x3 NumPy array
array2 = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]], dtype=np.float64)
array_multiply = array1 * array2
print(array_multiply)

# d) Print dtype, shape, and size of the result arrays
print("Array addition:", array_add)
print("Dtype:", array_add.dtype, "Shape:", array_add.shape, "Size:", array_add.size)
print("Array multiplication:", array_multiply)
print("Dtype:", array_multiply.dtype, "Shape:", array_multiply.shape, "Size:", array_multiply.size)

# Q2
# a) Create a DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [22, np.nan, 35, 17],
    "Salary": [5000, 6000, np.nan, 7000]
}
df = pd.DataFrame(data)

# b) Identify missing values using isna()
print("Missing values:")
print(df.isna())

# c) Drop rows with any missing data
df_dropped = df.dropna()
print("DataFrame after dropping missing values:")
print(df_dropped)

# d) Fill missing values with a specified value (mean for Age, 0 for Salary)
df_new = df.copy()
df_new["Age"].fillna(df["Age"].mean(), inplace=True)
df_new["Age"] = df_new["Age"].astype(int) # To convert the age to integer
df_new["Salary"].fillna(0, inplace=True)
print("DataFrame after filling missing values:")
print(df_new)

# 3. Matplotlib Visualisation
# a) to c) Create a simple line plot
time = np.arange(1, 11)  # X-axis (time steps)
values = np.random.randint(30, 100, 10)  # Random values for Y-axis
plt.figure(figsize=(8, 4))
plt.plot(time, values, color='blue', marker='o', linewidth=2, linestyle='--')
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Value Change Over Time")
plt.show()

# d) Create a scatter plot
age = np.random.randint(20, 60, 20)
income = np.random.randint(4000, 50000, 20)
plt.figure(figsize=(8, 4))
plt.scatter(age, income, color='red', alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Age vs Income")
plt.show()




