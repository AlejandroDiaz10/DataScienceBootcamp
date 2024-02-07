import numpy as np

# =================================================================== Base Functions
# Generating an array of 20 random integers between 0 and 20
numbers = np.random.randint(0, 21, 20)
print("\n*************** Base Functions ***************")
print("Original Array: \n", numbers)

# The sort() method in NumPy performs an in-place sort of the array and returns None.
numbers.sort()
print("\nSorted Array (in-place): \n", numbers)

# They first need to be already sorted (using sort())
numbers = numbers[::-1]
print("\nReversed Sorted Array (using sort()[::-1]): \n", numbers)

# =================================================================== Numpy Functions
# Generating another array of 20 random integers between 0 and 20
print("\n*************** Numpy Functions ***************")
numbers2 = np.random.randint(0, 21, 20)

# Using np.sort() to get a sorted array (not in-place)
sorted_array = np.sort(numbers2)
print("\nOriginal Array after np.sort(): \n", numbers2)
print("Sorted Array (np.sort()): \n", sorted_array)

# Reversing the sorted array
reversed_sorted_array = np.sort(numbers2)[::-1]
print("\nOriginal Array after np.sort()[::-1]: \n", numbers2)
print("Reversed Sorted Array (np.sort()[::-1]): \n", reversed_sorted_array)
