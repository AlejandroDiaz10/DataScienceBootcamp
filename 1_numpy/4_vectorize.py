import numpy as np


def add_10(number: int) -> int:
    return number + 10


# Generating a random array 'a' using np.random.randint
a = np.random.randint(0, 101, 10)

# Creating a vectorized function using np.vectorize with a named function 'add_10'
vector = np.vectorize(add_10)
# Creating a vectorized function using np.vectorize with a lambda function
vector2 = np.vectorize(lambda number: number + 10)

# Printing the original array 'a'
print(f"Original Array 'a': \n{a}")

# Applying the vectorized function 'add_10' to the array 'a'
print(f"\nVectorized with add_10: \n{vector(a)}")

# Applying the vectorized function with a lambda function to the array 'a'
print(f"\nVectorized with lambda function: \n{vector2(a)}")
