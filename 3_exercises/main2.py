import pandas as pd
import numpy as np

users_df = pd.read_csv("users.csv")
# print(users_df.head())

# =================================================================== Part 2
print("===================================== Part 2")

# Display in the console the name of all users whose age is in the range of 10 to 20 and 40 to 70.
print(
    "\n1) Display in the console the name of all users whose age is in the range of 10 to 20 and 40 to 70."
)
print(
    users_df[users_df["age"].between(10, 20) | users_df["age"].between(40, 70)][
        ["name", "age"]
    ]
)

# Display in the console all users with an email address.
print("\n2) Display in the console all users with an email address.")
print(users_df[users_df["email"].notnull()][["name", "email"]])

# Display on the screen the name and email of the youngest user in Canada.
print("\n3) Display on the screen the name and email of the youngest user in Canada.")
print(
    users_df[users_df["country"] == "Canada"]
    .sort_values(by="age")
    .head(1)[["name", "email", "age", "country"]]
)

# Display on the screen the name and email of the oldest user in Canada.
print("\n4) Display on the screen the name and email of the oldest user in Canada.")
print(
    users_df[users_df["country"] == "Canada"]
    .sort_values(by="age", ascending=False)
    .head(1)[["name", "email", "age", "country"]]
)

# List in the console the top 3 countries with the fewest users.
print("\n5) List in the console the top 3 countries with the fewest users.")
print(users_df.groupby("country")["country"].count().sort_values().head(3))

# Get the country with the highest number of users whose age is greater than 50.
print(
    "\n6) Get the country with the highest number of users whose age is greater than 50."
)
print(
    users_df[users_df["age"] > 50]
    .groupby("country")["country"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# Get the country with the highest average age.
print("\n7) Get the country with the highest average age.")
print(users_df.groupby("country")["age"].mean().sort_values(ascending=False).head(1))
# ---------------------------------------
# print(users_df.groupby("country")["age"].mean().idxmax())

# Display in the console the country with the most men.
print("\n8) Display in the console the country with the most men.")
print(
    users_df[users_df["gender"] == "male"]
    .groupby("country")["country"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# Display in the console the name, username, and age of all users whose age is greater than 10 and are not from the countries Mexico, Brazil, and Canada.
print(
    "\n9) Display in the console the name, username, and age of all users whose age is greater than 10 and are not from the countries Mexico, Brazil, and Canada."
)
countries = ["Mexico", "Brazil", "Canada"]
print(
    users_df[(users_df["age"] > 10) & (~users_df["country"].isin(countries))][
        ["name", "username", "age", "country"]
    ]
)

# Display in the console the postal code of all users from Mexico.
print("\n10) Display in the console the postal code of all users from Mexico.")
print(users_df[users_df["country"] == "Mexico"][["country", "postcode"]])

# Obtain the age that appears least frequently in the DataFrame.
print("\n11) Obtain the age that appears least frequently in the DataFrame.")
print(users_df.groupby("age")["age"].count().sort_values().head(1))

# Obtain the age that appears most frequently in the DataFrame.
print("\n12) Obtain the age that appears most frequently in the DataFrame.")
print(users_df.groupby("age")["age"].count().sort_values(ascending=False).head(1))
