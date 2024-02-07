# Numerical Python -> Powerful library in Python for numerical and mathematical operations
import numpy as np

"""
Multidimensional array that provides a flexible and efficient way to represent and manipulate 
numerical data. It is similar to a Python list, but with some key differences:

1) Homogeneous Data Type: 
    All elements in a NumPy array must be of the same data type
2) Fixed Size: 
    The size of a NumPy array is fixed upon creation. Once an array is created, its size cannot be changed.
3) Vectorized Operations
    NumPy arrays support vectorized operations, meaning that operations can be performed on entire 
    arrays at once without the need for explicit loops. This makes numerical computations more 
    efficient and concise.
"""

# =================================================================== Common initialization functions
print("*************** Common initialization functions ***************")
# Creating arrays with zeros
zeros_array = np.zeros((3, 4))  # 3x4 array filled with zeros
print(f"Zeros Array: \n{zeros_array}")

# Creating arrays with ones
ones_array = np.ones((2, 3))  # 2x3 array filled with ones
print(f"\nOnes Array: \n{ones_array}")

# Creating an identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix
print(f"\nIdentity Matrix: \n{identity_matrix}")

# =================================================================== Array attributes
print("\n\n*************** Array attributes ***************")
nums = np.array([1, 2, 3, 4, 5])
print(f"Array: {nums}")

# Size (total number of elements)
print("\nTotal number of elements in nums:", nums.size)

# Shape of the array: Tuple that represents the number of elements along each dimension
print("Shape of nums:", nums.shape)

# Data type of the array
print("Data type of nums:", nums.dtype)

# Number of dimensions
print("Number of dimensions in nums:", nums.ndim)


# =================================================================== Element-wise operations
print("\n\n*************** Element-wise operations ***************")
print(f"Original Array: \t\t{nums}")
nums_added = nums + 20
print(f"Added Array (+20): \t\t{nums_added}")
nums_subtracted = nums - 20
print(f"Subtracted Array (-20): \t{nums_subtracted}")
nums_multiplied = nums * 20
print(f"Multiplied Array (*20): \t{nums_multiplied}")
nums_divided = nums / 2
print(f"Divided Array (/20): \t\t{nums_divided}")
nums_squared = nums**2
print(f"Squared Array (^2): \t\t{nums_squared}")


# =================================================================== Array-wise operations
print("\n\n*************** Array-wise operations ***************")
nums2 = np.array([10, 20, 30, 40, 50])

print(f"Array 1: \t\t{nums}")
print(f"Array 2: \t\t{nums2}")

# Matrix multiplication
matrix_product = np.dot(nums, nums2)
print(f"\nMatrix Product: \t\t\t{matrix_product}")

addition_of_arrays = nums + nums2
print(f"Addition of arrays (A1 + A2): \t\t{addition_of_arrays}")

subtraction_product = nums2 - nums
print(f"Susbtraction of arrays (A2 - A1): \t{subtraction_product}")
