import pandas as pd
import numpy as np

"""
SERIES
A Series is a one-dimensional labeled array capable of holding any data type. 
It is similar to a column in a spreadsheet or a dataset in R. 
A Series can be seen as a specialized dictionary or a column in a table.

Key characteristics of a Pandas Series:
* Indexing: Each element in a Series has an associated index, which is a label or a name. The index provides a way to access the data.
* Homogeneous Data: A Series can contain data of any data type, but all elements within the Series must be of the same data type. 
* Size Immutability: Once a Series is created, you cannot change its size. You can, however, modify the values within it.
* Operations: Series supports vectorized operations and functions, making it convenient for mathematical and statistical operations.
"""

# =================================================================== Series attributes
# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data, name="MySeries")

# Displaying the Series
print("\n*************** Series Attributes ***************")
print("Series:\n", series)
print("\nSize of Series: ", series.size)
print("Data Type of Series: ", series.dtype)
print("Shape of Series: ", series.shape)
print("Index of Series: ", series.index)

# =================================================================== Accessing elements
print("\n*************** Accessing Elements ***************")
print("Element at index 0: ", series[0])

# Modifying an element
series[0] = 100
print("Modified Series:\n", series)

# =================================================================== Indexing
indeces = ["a", "b", "c", "d", "e"]
series2 = pd.Series(data, index=indeces, name="MySeries2", dtype=float)
print("\n*************** Indexing ***************")
print("Series with Custom Index:\n", series2)

# Modifying an element using custom index
series2["a"] = 120
print("\nModified Series with Custom Index:\n", series2)

# =================================================================== Create series (dictionaries)
colors = {"red": 10, "white": 20, "blue": 30, "black": 40, "green": 50}
color_series = pd.Series(colors, name="Colors")
print("\n*************** Creating Series from Dictionaries ***************")
print("Color Series:\n", color_series)

# =================================================================== Null values (NaN -> Not a Number)
null_values_series = pd.Series(
    [1, 2, 3, np.nan, np.nan, 6, 7, np.nan, 9, 10], name="NullValues"
)
print("\n*************** Null Values (NaN) ***************")
print("Series with Null Values:\n", null_values_series)

# isnull: Returns a boolean series (true if value is NaN)
print("\n*************** isnull ***************")
print("\nisnull():\n", null_values_series.isnull())
print(
    "\nNull Values using isnull():\n", null_values_series[null_values_series.isnull()]
)

# notnull: Returns a boolean series (true if value is not NaN)
print("\n*************** notnull ***************")
print("\nnotnull():\n", null_values_series.notnull())
print(
    "\nNonNull Values using notnull():\n",
    null_values_series[null_values_series.notnull()],
)
