import pandas as pd
import numpy as np

users_df = pd.read_csv("users.csv")
# print(users_df.head())

# =================================================================== Part 1
# Get the name and email of all users.
# print(users_df[["name", "email"]])

# Get the name of all users whose gender is Female.
# print(users_df[users_df["gender"] == "female"][["name", "gender"]])

# Get the name of all users whose gender is Male and have an age greater than 50.
# print(
#     users_df[(users_df["gender"] == "male") & (users_df["age"] > 50)][
#         ["name", "gender", "age"]
#     ]
# )

# Get all users whose age is greater than 68.
# print(users_df[users_df["age"] > 68][["name", "age"]])

# Get the username and email of users whose age is in the range 40 to 60.
# print(users_df[users_df["age"].between(40, 60)][["name", "email", "age"]])

# Get the username of all users whose email does not end with @example.com.
# print(users_df[~users_df["email"].str.endswith("@example.com")][["name", "email"]])

# Get the username of all users whose country is Germany, Finland, or Canada.
# countries = ["Germany", "Finland", "Canada"]
# print(users_df[users_df["country"].isin(countries)][["name", "country"]])

# Get the name and email of all female users from Germany.
# print(
#     users_df[(users_df["gender"] == "female") & (users_df["country"] == "Germany")][
#         ["name", "gender", "country"]
#     ]
# )

# Get the average age of all female users from Canada older than 20 years.
# condition = (
#     (users_df["country"] == "Canada")
#     & (users_df["gender"] == "female")
#     & (users_df["age"] > 20)
# )
# print(users_df.age[condition].mean())
# ---------------------------------------
# print(
#     users_df[
#         (users_df["gender"] == "female")
#         & (users_df["country"] == "Canada")
#         & (users_df["age"] > 20)
#     ]["age"].mean()
# )

# Know the number of users residing in Finland.
# print(users_df[users_df["country"] == "Finland"]["name"].count())

# Display in the console the number of men and women in the dataframe.
# print(users_df.groupby("gender")["gender"].count())

# Display in the console the country with the most women.
# print(
#     users_df[users_df["gender"] == "female"]
#     .groupby("country")["country"]
#     .count()
#     .sort_values(ascending=False)
#     .head(1)
# )

# Get the top 3 countries with the most users.
# print(users_df.groupby("country")["country"].count().sort_values(ascending=False).head(3))
# print(users_df.groupby("country")["country"].count().sort_values().tail(3)[::-1])


# =================================================================== Part 2
# Display in the console the name of all users whose age is in the range of 10 to 20 and 40 to 70.
# Display in the console all users with an email address.
# Display on the screen the name and email of the youngest user in Canada.
# Display on the screen the name and email of the oldest user in Canada.
# List in the console the top 3 countries with the fewest users.
# Get the country with the highest number of users whose age is greater than 50.
# Get the country with the highest average age.
# Display in the console the country with the most men.
# Display in the console the name, username, and age of all users whose age is greater than 10 and are not from the countries Mexico, Brazil, and Canada.
# Display in the console the postal code of all users from Mexico. Obtain the age that appears most frequently in the DataFrame.
# Obtain the age that appears least frequently in the DataFrame.
