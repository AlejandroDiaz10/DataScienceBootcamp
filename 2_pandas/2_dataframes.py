import pandas as pd

"""
A DataFrame is a two-dimensional labeled data structure in Pandas, similar to a table in a relational database or a spreadsheet in Excel. 
It consists of rows and columns, where each column can have a different data type. 

The main features of a Pandas DataFrame include:
* Tabular Structure: DataFrames are organized in a tabular structure with rows and columns, allowing for easy visualization and manipulation of data.
* Column Labels (Column Index): Each column in a DataFrame has a label or name. Column labels are used to access and manipulate specific columns.
* Row Labels (Row Index): Each row in a DataFrame has an index, which can be a numeric index or a set of labels. The index allows for easy access to and retrieval of specific rows.
* Mixed Data Types: DataFrames can contain columns with different data types. This flexibility makes them suitable for handling diverse datasets.
* Missing Data Handling: DataFrames provide tools for handling missing or NaN (Not a Number) values, making them robust for real-world datasets.
* Operations and Methods: DataFrames support a wide range of operations and methods for data analysis, transformation, filtering, grouping, and merging, among others.
"""

# =================================================================== Create dataframe (dictionaries)
# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28],
    "City": ["New York", "San Francisco", "Los Angeles", "Chicago"],
}

# Creating a DataFrame without custom indices
df = pd.DataFrame(data)

# Displaying the DataFrame
print("\n*************** Create DataFrame (Dictionaries) ***************")
print("DataFrame from Dictionary:\n", df)

# =================================================================== Indexing
indeces = ["a", "b", "c", "d"]
df2 = pd.DataFrame(data, index=indeces)

# Assigning a name to the DataFrame
df2.name = "MyDataFrame"
print("\n*************** Indexing ***************")
print("DataFrame with Custom Index (and Name):\n", df2)

# =================================================================== Accesing elements
print("\n*************** Accessing Elements ***************")
# Returns a Series -> Format recommended
print("Accessing 'Name' column:\n", df["Name"])
print("\nType of 'Name' column:\n", type(df["Name"]))

# Returns a Series
print("Accessing 'City' column:\n", df.City)
print("Type of 'City' column:", type(df.City))

# =================================================================== Columns and values
print("\n*************** Columns and Values ***************")
print("Column labels:\n", df.columns)
print("\nValues in DataFrame:\n", df.values)
