import numpy as np

# =================================================================== Matrix attributes
print("\n*************** Matrices in NumPy ***************")

# Creating a Matrix:
matrix_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2x3 Matrix (matrix_2x3): \n{matrix_2x3}")

# Shape and Dimensions:
matrix_shape = matrix_2x3.shape
matrix_dimensions = matrix_2x3.ndim
print(f"\nMatrix Shape: {matrix_shape}, Dimensions: {matrix_dimensions}")

# =================================================================== Relevant operations
print("\n*************** Relevant operations ***************")
# Accessing Elements in a Matrix:
element_at_1_2 = matrix_2x3[1, 2]
element_at_1_2_2 = matrix_2x3[1][2]
print(f"\nElement at Row 1, Column 2: {element_at_1_2}")
print(f"Element at Row 1, Column 2: {element_at_1_2_2}")

# Identity Matrix:
identity_matrix = np.eye(3)
print(f"\n3x3 Identity Matrix: \n{identity_matrix}")

# Slicing a Matrix:
submatrix = matrix_2x3[:, 1:]
column_1 = matrix_2x3[:, 1]
first_last = matrix_2x3[0, [0, 2]]
print(f"\nSubmatrix (all rows, columns 2 and 3): \n{submatrix}")
print(f"\nSubmatrix (column 1): \n{column_1}")
print(f"\nSubmatrix (first and last numbers in row 1): \n{first_last}")

# =================================================================== Matrix Operations
print("\n*************** Matrix operations ***************")
# Transpose
transposed_matrix = matrix_2x3.T
print(f"\nTransposed Matrix: \n{transposed_matrix}")

# Matrix Multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print(f"\nMatrix A: \n{matrix_a}")
print(f"Matrix B: \n{matrix_b}")
print(f"Matrix Product (A x B): \n{matrix_product}")

# =================================================================== Manipulating Matrices
print("\n*************** Manipulating Matrices ***************")

# Adding a Scalar to a Matrix
scalar_added_matrix = matrix_2x3 + 10
print(f"\nMatrix with Scalar Added: \n{scalar_added_matrix}")

# Element-wise Operations
elementwise_squared_matrix = matrix_2x3**2
print(f"\nElement-wise Squared Matrix: \n{elementwise_squared_matrix}")
