import numpy as np

"""
COPY
A copy is a new array or object with its own data that is completely independent of the 
original array. Modifying the copy does not affect the original array, and vice versa.

VIEW
A view is an array that shares its data with another array, but it can have a different 
shape or strides. Changes to the data in the view affect the original array, and 
vice versa.

* Copies are Independent: Modifications to a copy do not affect the original array.
* Views are Linked: Modifications to a view affect the original array, and vice versa.
* Memory Efficiency: Views are memory-efficient as they share data with the original array.
* Performance Consideration: Creating a copy requires more memory and time compared to creating a view.
"""

original_array = np.arange(1, 11)
array_copy = original_array.copy()
array_view = original_array.view()
# array_view2 = original_array[:]

print(f"Original Array (original_array): \n{original_array}")

# Modifying the copy does not affect the original array
array_copy[0] = -1
print(f"\nModified Copy (array_copy): \n{original_array}")

# Modifying the view affects the original array
array_view[0] = -1
print(f"\nModified View (array_view): \n{original_array}")

# Slicing and indexing can create views of the original array
subarray_view = original_array[1:4]
subarray_view[1] = -1
print(f"\nModified Subarray View (subarray_view): \n{original_array}")

# Checking if an Array is a Copy or a View
# If an array is a view, the base attribute will point to the original array
print(f"\nIs array_copy a view? {array_copy.base is original_array}")
print(f"Is array_view a view? {array_view.base is original_array}")

# Printing memory addresses (IDs) to demonstrate identity
print(f"\nID of original_array:  {id(original_array)}")
print(f"ID of array_copy.base: {id(array_copy.base)}")
print(f"ID of array_view.base: {id(array_view.base)}")
