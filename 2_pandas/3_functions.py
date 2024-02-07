import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28],
    "City": ["New York", "San Francisco", "Los Angeles", "Chicago"],
}

# Creating a DataFrame without custom indices
df = pd.DataFrame(data)

print("\n*************** Initial DataFrame ***************")
print(df)

# =================================================================== Create a df column (series)
# Best option
df["Job"] = ["Engineer", "Data Scientist", "Designer", "Teacher"]
print("\n*************** Create DataFrame Column (Series) ***************")
print("DataFrame with 'Job' Column:\n", df)

# Another option using a Series
job_column = pd.Series(["Engineer", "Data Scientist", "Designer", "Teacher"])
df["Job2"] = job_column
print("\nDataFrame with Additional 'Job2' Column (from Series):\n", df)

# =================================================================== Rename df columns (not in-place)
df = df.rename(columns={"Job2": "SecondJob"})
print("\n*************** Rename DataFrame Columns ***************")
print("DataFrame with Renamed 'Job2' to 'SecondJob':\n", df)

# =================================================================== Delete df columns (in-place)
del df["SecondJob"]
print("\n*************** Delete DataFrame Columns (In-Place) ***************")
print("DataFrame after Deleting 'SecondJob' Column:\n", df)
