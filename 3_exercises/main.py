import pandas as pd
import numpy as np

users_df = pd.read_csv("users.csv")
# print(users_df.head())

# =================================================================== Part 1
print("===================================== Part 1")

# Get the name and email of all users.
print("\n1) Get the name and email of all users.")
print(users_df[["name", "email"]])

# Get the name of all users whose gender is Female.
print("\n2) Get the name of all users whose gender is Female.")
print(users_df[users_df["gender"] == "female"][["name", "gender"]])

# Get the name of all users whose gender is Male and have an age greater than 50.
print(
    "\n3) Get the name of all users whose gender is Male and have an age greater than 50."
)
print(
    users_df[(users_df["gender"] == "male") & (users_df["age"] > 50)][
        ["name", "gender", "age"]
    ]
)

# Get all users whose age is greater than 68.
print("\n4) Get all users whose age is greater than 68.")
print(users_df[users_df["age"] > 68][["name", "age"]])

# Get the username and email of users whose age is in the range 40 to 60.
print("\n5) Get the username and email of users whose age is in the range 40 to 60.")
print(users_df[users_df["age"].between(40, 60)][["name", "email", "age"]])

# Get the username of all users whose email does not end with @example.com.
print("\n6) Get the username of all users whose email does not end with @example.com.")
print(users_df[~users_df["email"].str.endswith("@example.com")][["name", "email"]])

# Get the username of all users whose country is Germany, Finland, or Canada.
print(
    "\n7) Get the username of all users whose country is Germany, Finland, or Canada."
)
countries = ["Germany", "Finland", "Canada"]
print(users_df[users_df["country"].isin(countries)][["name", "country"]])

# Get the name and email of all female users from Germany.
print("\n8) Get the name and email of all female users from Germany.")
print(
    users_df[(users_df["gender"] == "female") & (users_df["country"] == "Germany")][
        ["name", "gender", "country"]
    ]
)

# Get the average age of all female users from Canada older than 20 years.
print("\n9) Get the average age of all female users from Canada older than 20 years.")
condition = (
    (users_df["country"] == "Canada")
    & (users_df["gender"] == "female")
    & (users_df["age"] > 20)
)
print(users_df.age[condition].mean())
# ---------------------------------------
# print(
#     users_df[
#         (users_df["gender"] == "female")
#         & (users_df["country"] == "Canada")
#         & (users_df["age"] > 20)
#     ]["age"].mean()
# )

# Know the number of users residing in Finland.
print("\n10) Know the number of users residing in Finland.")
print(users_df[users_df["country"] == "Finland"]["name"].count())

# Display in the console the number of men and women in the dataframe.
print("\n11) Display in the console the number of men and women in the dataframe.")
print(users_df.groupby("gender")["gender"].count())

# Display in the console the country with the most women.
print("\n12) Display in the console the country with the most women.")
print(
    users_df[users_df["gender"] == "female"]
    .groupby("country")["country"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# Get the top 3 countries with the most users.
print("\n13) Get the top 3 countries with the most users.")
print(
    users_df.groupby("country")["country"].count().sort_values(ascending=False).head(3)
)
# ---------------------------------------
# print(users_df.groupby("country")["country"].count().sort_values().tail(3)[::-1])
