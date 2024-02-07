import numpy as np

# Generating an array of 10 random integers between 0 and 10
numbers = np.random.randint(0, 11, 10)
print("\nOriginal Array (numbers): \n", numbers)
print(f"Size of Original Array: {numbers.size}")

# =================================================================== Functions: insert & append
print("\n*************** Functions: insert & append ***************")

# Inserting 200 at the beginning of a new array
numbers2 = np.insert(numbers, 0, 200)
print("\nOriginal Array (numbers): \n", numbers)
print("Array after Insertion at index 0 (numbers2): \n", numbers2)

# Appending 200 to the end of a new array
numbers3 = np.append(numbers, 200)
print("\nOriginal Array (numbers): \n", numbers)
print("Array after Append (numbers3): \n", numbers3)

# =================================================================== Function: delete
print("\n*************** Function: delete ***************")

# Deleting the last element in a new array
numbers4 = np.delete(numbers, -1)
print("\nOriginal Array (numbers): \n", numbers)
print("Array after Deletion (numbers4): \n", numbers4)

# =================================================================== Function: resize
print("\n*************** Function: resize ***************")

# Creating a new resized array
resized_array = np.resize(numbers, 15)
print("\nResized Array (resized_array): \n", resized_array)
print(f"Size of Resized Array: {resized_array.size}")
print("Size of Original Array (numbers):", numbers.size)

# Resizing the original array in-place
numbers.resize(5)
print("\nResized Array In-Place (numbers): \n", numbers)
print(f"Size of Resized Array In-Place: {numbers.size}")

# =================================================================== Function: concatenate
print("\n*************** Function: concatenate ***************")

# Generating another array of 10 random integers
numbers_2 = np.random.randint(0, 11, 10)

# Concatenating two arrays to create a new array
new_array = np.concatenate([numbers, numbers_2])
print("\nConcatenated Array (new_array): \n", new_array)
