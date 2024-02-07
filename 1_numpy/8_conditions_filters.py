import numpy as np

# Generating an array of 20 random integers between 0 and 100
numbers = np.random.randint(0, 101, 20)

# =================================================================== Relevant filters
print("\n*************** Relevant Filters ***************")
# Displaying the original array
print(f"Original Array: \n{numbers}")

# Filtering elements greater than 50
print(f"\nElements > 50: \n{numbers > 50}")

# Extracting elements greater than 50
print(f"\nExtracted Elements > 50: \n{numbers[numbers > 50]}")

# Filtering elements between 50 and 90
print(f"\nElements between 50 and 90: \n{numbers[(numbers > 50) & (numbers < 90)]}")

# Filtering elements less than 20 or greater than 80
print(f"\nElements < 20 or > 80: \n{numbers[(numbers < 20) | (numbers > 80)]}")

# =================================================================== Functions: all & any
print("\n*************** Functions: all & any ***************")
# All: Checks if all elements along a specified axis or in the entire array satisfy a given condition.
# Checking if all elements are greater than 40
print(f"\nAll elements > 40: {np.all(numbers > 40)}")

# Checking if all elements are greater than or equal to 0
print(f"All elements >= 0: {np.all(numbers >= 0)}")

# Any: Checks if any element along a specified axis or in the entire array satisfies a given condition.
# Checking if any element is greater than 100
print(f"Any element > 100: {np.any(numbers > 100)}")

# Checking if any element is greater than 40
print(f"Any element > 40: {np.any(numbers > 40)}")

# =================================================================== Functions: where & select
print("\n*************** Functions: where & select ***************")
# Generating an array of 10 random integers between 1 and 10
grades = np.random.randint(1, 11, 10)
print(f"\nGrades Array: \n{grades}")

# Where: Returns the indices of elements that satisfy a given condition
# Where: Getting the indices of elements greater than or equal to 7
indices = np.where(grades >= 7)
grades_results = np.where(grades >= 7, "Approved", "Failed")
print(f"\nIndices >= 7: \n{indices}")
print(f"Results based on Grades: \n{grades_results}")

# Select: Returns an array drawn from elements in choices, depending on conditions.
# Select: Assigning messages based on different conditions
conditions = [grades == 10, ((grades >= 8) & (grades < 10)), grades == 7, grades < 7]
messages = ["Perfect", "Exceptional", "Good", "Bad"]
result = np.select(conditions, messages)
print(f"\nResults based on Conditions: \n{result}")
