import pandas as pd

# Assuming you have a CSV file named "users.csv" with an "id" column as the index
users_df = pd.read_csv("users.csv", index_col="id")
print("\n*************** Initial DataFrame ***************")
print(users_df.head())
print(users_df.tail())

# =================================================================== Data cleaning
# Delete rows with missing data
clean_users_df = users_df.dropna()
print("\n*************** Data Cleaning: Delete Rows with Missing Data ***************")
print("DataFrame after Dropping Rows with Missing Data:\n", clean_users_df)

# Forced imputation
imputed_users_df = users_df.fillna("New value")
print("\n*************** Data Cleaning: Forced Imputation ***************")
print("DataFrame after Forced Imputation with 'New value':\n", imputed_users_df)

# Forced imputation with dictionaries
imputed_users_df2 = users_df.fillna({"name": "No name", "email": "example@example.com"})
print(
    "\n*************** Data Cleaning: Forced Imputation with Dictionaries ***************"
)
print("DataFrame after Forced Imputation with Dictionaries:\n", imputed_users_df2)
