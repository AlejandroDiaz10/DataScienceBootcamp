import numpy as np

# =================================================================== Arrays
# savetxt & loadtxt work with plain text files
# Generating an array of 10 random integers between 0 and 10
numbers = np.random.randint(0, 11, 10)
print("\n*************** Arrays ***************")
print(f"Original Array (numbers): \n{numbers}")

# Saving the array to a text file ("array.txt")
np.savetxt("array.txt", numbers, fmt="%i")

# Loading the array from the text file
numbers_float = np.loadtxt("array.txt")
print(f"\nLoaded Array from 'array.txt' (numbers_float): \n{numbers_float}")
print(f"Dtype of Loaded Array: {numbers_float.dtype}")

# Loading the array with a specified dtype (int)
numbers2 = np.loadtxt("array.txt", dtype=int)
print(f"\nLoaded Array from 'array.txt' with dtype=int (numbers2): \n{numbers2}")
print(f"Dtype of Loaded Array with dtype=int: {numbers2.dtype}")

# =================================================================== Matrices
# Reshaping the array into a 2x5 matrix
matrix = numbers.reshape(2, 5)
print("\n*************** Matrices ***************")
print(f"Reshaped Matrix (2x5) from 'numbers' (matrix): \n{matrix}")

# Saving the matrix to a CSV file ("matrix.csv")
np.savetxt("matrix.csv", matrix, delimiter=",", fmt="%i")

# Loading the matrix from the CSV file
matrix2 = np.loadtxt("matrix.csv", delimiter=",", dtype=int)
print(f"\nLoaded Matrix from 'matrix.csv' (matrix2): \n{matrix2}")

# =================================================================== Functions: save & load
# save & load work with binary files
print("\n*************** Functions: save & load ***************")

# Saving the array to a binary file ("binary_array.npy")
np.save("binary_array.npy", numbers)

# Loading the array from the binary file
binary_numbers = np.load("binary_array.npy")
print(f"\nLoaded Array from 'binary_array.npy' (binary_numbers): \n{binary_numbers}")

# Saving the matrix to a binary file ("binary_matrix.npy")
np.save("binary_matrix.npy", matrix)

# Loading the matrix from the binary file
binary_matrix = np.load("binary_matrix.npy")
print(f"\nLoaded Matrix from 'binary_matrix.npy' (binary_matrix): \n{binary_matrix}")
