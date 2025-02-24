import numpy as np

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
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype)
print(arr2.itemsize)