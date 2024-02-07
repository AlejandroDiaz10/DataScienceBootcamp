import pandas as pd

"""
LOC -> string
loc is label-based indexing, which means you specify the names of the rows and columns to select.
It is used when you want to select data based on labels (index and column names).
The syntax is df.loc[row_labels, column_labels].

ILOC -> int
iloc is integer-location based indexing, which means you specify the numerical indices of the rows and columns to select.
It is used when you want to select data based on integer positions.
The syntax is df.iloc[row_indices, column_indices].
"""

# Assuming you have a DataFrame named df
df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
        "Age": [25, 30, 35, 28, 22, 40],
        "City": [
            "New York",
            "San Francisco",
            "Los Angeles",
            "Chicago",
            "Boston",
            "Seattle",
        ],
    },
    index=["id1", "id2", "id3", "id4", "id5", "id6"],
)

print(df)

# =================================================================== Using loc
print("\n*************** Using loc ***************")
# Selecting a specific row using loc
selected_row_loc = df.loc["id1"]
print("\nSelected Row using loc:")
print(selected_row_loc)

# Selecting a specific value using loc
selected_data_loc = df.loc["id1", "Age"]
print("\nSelected Data using loc:", selected_data_loc)

# Selecting a range of rows using loc
sub_dataframe_loc = df.loc["id2":"id4"]
print("\nSub-DataFrame using loc (Range of Rows):")
print(sub_dataframe_loc)

# Selecting specific columns for a range of rows using loc
sub_dataframe_loc2 = df.loc["id2":"id4", ["Name", "City"]]
print("\nSub-DataFrame using loc (Range of Rows and Columns):")
print(sub_dataframe_loc2)

# Selecting specific columns for a range of rows using loc (alternative syntax)
sub_dataframe_loc3 = df.loc["id2":"id4"][["Name", "City"]]
print("\nSub-DataFrame using loc (Alternative Syntax):")
print(sub_dataframe_loc3)

# =================================================================== Using iloc
print("\n*************** Using iloc ***************")
# Selecting a specific row using iloc
selected_row_iloc = df.iloc[0]
print("\nSelected Row using iloc:")
print(selected_row_iloc)

# Selecting a specific value using iloc
selected_data_iloc = df.iloc[0, 1]
print("\nSelected Data using iloc:", selected_data_iloc)

# Selecting a range of rows using iloc
sub_dataframe_iloc = df.iloc[1:4]
print("\nSub-DataFrame using iloc (Range of Rows):")
print(sub_dataframe_iloc)

# Selecting specific columns for a range of rows using iloc
sub_dataframe_iloc2 = df.iloc[1:4, [0, 2]]
print("\nSub-DataFrame using iloc (Range of Rows and Columns):")
print(sub_dataframe_iloc2)

# Selecting specific columns for a range of rows using iloc (alternative syntax)
sub_dataframe_iloc3 = df.iloc[1:4][["Name", "City"]]
print("\nSub-DataFrame using iloc (Alternative Syntax):")
print(sub_dataframe_iloc3)
