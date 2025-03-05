import numpy as np

# To comment all: Shift + Alt + A

arr = np.array([1,2,3])
# print(arr)

# array with 2 arrays
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# array with 2 arrays
# array with 2 arrays
arr3 = np.array(
    [
        [[1,2],[3,4]],
        [[5,6],[7,8]]
    ]
)
# print(arr3)

print(arr2.shape)
print(arr2.ndim) # no of rows
print(arr2.size) # no of column
print(arr2.dtype)
print(arr2.itemsize)
print(arr3.reshape(4,2)) # reshape into 3 rows and 2 column
sum = arr + arr2
product = arr * arr2
power = arr ** 2
sqrt = np.sqrt(arr)
print(power)
print(sqrt)

# linspace will include 1 in the range
lineSpace=np.linspace(0,10,5)
print(lineSpace)


# rows: days, cols: cities
temps = np.array(
    [
        [30,32,29],
        [31,33,30],
        [29,30,28],
        [35,36,34],
        [28,27,26],
        [32,31,33],
        [30,29,28]
    ]
)

# max temp per city
max_temp = np.max(temps,axis=0) # axis = 0 means vertical axis not column 0
print("max temp per city ", max_temp)

coldest_city = np.argmin(np.mean(temps,axis=0)) # argmin Returns the indices of the minimum values along an axis.
print("coldest city ", coldest_city)

std_dev = np.std(temps,axis=0)
print("standard deviation ", std_dev)

above_35_days = np.where(temps>35)
print("days above 35", above_35_days) # days above 35 (array([3]), array([1])) means go to column 3 and row 1

sorted_array = np.sort(temps,axis=0)
print(sorted_array)