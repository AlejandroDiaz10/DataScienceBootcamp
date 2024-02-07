import numpy as np

# =================================================================== Function: np.arange
print("\n*************** Function: np.arange ***************")
# Creating an array 'a' from 0 to 10 (exclusive)
a = np.arange(0, 11)
print(f"\nArray 'a': \n{a}")

# Creating an array 'b' from 0 to 10 (exclusive) with a step of 2
b = np.arange(0, 11, 2)
print(f"\nArray 'b' (even numbers): \n{b}")

# =================================================================== Creating matrices
print("\n*************** Creating matrices ***************")
# Creating arrays with zeros
zeros_array = np.zeros((3, 4))  # 3x4 array filled with zeros
print(f"Zeros Array: \n{zeros_array}")

# Creating arrays with ones
ones_array = np.ones((2, 3))  # 2x3 array filled with ones
print(f"\nOnes Array: \n{ones_array}")

# Creating an identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix
print(f"\nIdentity Matrix: \n{identity_matrix}")

# =================================================================== Creating ndarrays
print("\n*************** Creating ndarrays ***************")
# Creating arrays with zeros and specifying dtype
zeros = np.zeros(10)
print(f"\nZeros Array: \n{zeros}")
print(f"Dtype of 'zeros': {zeros.dtype}")

zeros2 = np.zeros(10, dtype=int)
print(f"\nZeros Array with dtype=int: \n{zeros2}")
print(f"Dtype of 'zeros2': {zeros2.dtype}")

# Creating arrays with ones and specifying dtype
ones = np.ones(10)
print(f"\nOnes Array: \n{ones}")
print(f"Dtype of 'ones': {ones.dtype}")

ones = np.ones(10, dtype=int)
print(f"\nOnes Array with dtype=int: \n{ones}")
print(f"Dtype of 'ones': {ones.dtype}")

# Creating a constant array with np.full
constant_value = 7.5
array_shape = (12,)
constant_array = np.full(array_shape, constant_value)
print(f"\nConstant Array: \n{constant_array}")
print(f"Dtype of 'constant_array': {constant_array.dtype}")

# Creating an empty array with np.empty
trash_values = np.empty(10)
print(f"\nEmpty Array: \n{trash_values}")
print(f"Dtype of 'trash_values': {trash_values.dtype}")

# Creating a random array with np.random.randint
random_array = np.random.randint(0, 50, 20)
print(f"\nRandom Array: \n{random_array}")

# =================================================================== Creating subarrays
print("\n*************** Creating subarrays ***************")
print(f"Original Array: \n{a}")

# Creating arrays with zeros and specifying dtype
sub_a = a[0:5]
print(f"\nSubarray 'sub_a': \n{sub_a}")

sub_a2 = a[0 : len(a) : 2]
print(f"\nSubarray 'sub_a2': \n{sub_a2}")

sub_a3 = a[[0, 4, 8]]
print(f"\nSubarray 'sub_a3': \n{sub_a3}")

sub_a4 = a[[True, False, False, False, True, False, False, False, True, False, False]]
print(f"\nSubarray 'sub_a4': \n{sub_a4}")
