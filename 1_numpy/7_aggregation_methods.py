import numpy as np

# Creating an Array for Demonstration
data_array = np.array([3, 7, 1, 9, 4, 6, 8, 2, 5])

# # =================================================================== Common Aggregation Methods
print("\n*************** Common Aggregation Methods ***************")
# Sum
array_sum = np.sum(data_array)
print(f"\nSum of Array Elements: {array_sum}")

# Mean (Average)
array_mean = np.mean(data_array)
print(f"Mean of Array Elements: {array_mean}")

# Minimum and Maximum
array_min = np.min(data_array)
array_max = np.max(data_array)
print(f"Minimum Value: {array_min}, Maximum Value: {array_max}")

# Standard Deviation and Variance
array_std = np.std(data_array)
array_var = np.var(data_array)
print(f"Standard Deviation: {array_std}, Variance: {array_var}")

# # =================================================================== Aggregation Along an Axis (for Multidimensional Arrays)
print("\n*************** for Multidimensional Arrays ***************")
# Creating a 2D Array for Demonstration
matrix_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2x3 Matrix for Aggregation: \n{matrix_2x3}")

sum_row_1 = matrix_2x3[1].sum()
print(f"\nRow 1 Sum: {sum_row_1}")

sum_column_1 = matrix_2x3[:, 1].sum()
print(f"Column 1 Sum: {sum_column_1}")

# Sum along columns (axis=0)
column_sum = np.sum(matrix_2x3, axis=0)
print(f"Column-wise Sum: {column_sum}")

# Sum along rows (axis=1)
row_sum = np.sum(matrix_2x3, axis=1)
print(f"Row-wise Sum: {row_sum}")

# ===================================================================
