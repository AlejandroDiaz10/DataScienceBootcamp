import pandas as pd

# Read the csv
users_df = pd.read_csv("users.csv", index_col="id")
# print(users_df.head())
# print(users_df.describe())
# print(users_df.info())

# Clean de df (drop null values)
users_df = users_df.dropna()
print(users_df.info())


# =================================================================== Intro exercises
# 1) Get the name of all users from the country Canada.
canadian_users = users_df[users_df["country"] == "Canada"]["name"]
print("\n1) Canadian users:\n", canadian_users)

# 2) Get the name and email of all users older than 50 years old.
users_over_50 = users_df[users_df["age"] > 50][["name", "email"]]
print("\n2) Users over 50 years:\n", users_over_50)

# 3) Obtain the average age of all female users with an age greater than 30.
women_age_average = users_df[(users_df["gender"] == "female") & (users_df["age"] > 30)][
    "age"
].mean()
print("\n3) Average age of female users over 30:\n", f"{women_age_average:.2f}")


# =================================================================== Sorting
# 4) Get the youngest user from the country Canada.
youngest_canadian_person = (
    users_df[users_df["country"] == "Canada"].sort_values("age").head(1)
)
# youngest_canadian_person = users_df[users_df["country"] == "Canada"].sort_values("age").iloc[0]
print("\n4) Youngest Canadian person:\n", youngest_canadian_person)

# 5) Retrieve the 5 oldest users from Germany.
oldest_german_people = (
    users_df[users_df["country"] == "Germany"]
    .sort_values("age", ascending=False)
    .head()
)
# oldest_german_people = (
#     users_df[users_df["country"] == "Germany"]
#     .sort_values("age", ascending=False)
#     .iloc[0:5]
# )
print("\n5) Oldest German people:\n", oldest_german_people)


# =================================================================== Functions: between, isin
# 6) Retrieve all users between the ages of 40 and 50
# users_40_50 = users_df[(users_df["age"] >= 40) & (users_df["age"] <= 50)][["name", "age"]]
users_40_50 = users_df[users_df["age"].between(40, 50)][["name", "age"]]
print("\n6) Users between 40 and 50 years old:\n", users_40_50)

# 7) Retrieve the name of all users older than 30 years from the countries Canada, Germany, and France
countries = ["Canada", "Germany", "France"]
first_world_users = users_df[
    (users_df["age"] > 30) & (users_df["country"].isin(countries))
][["name", "age", "country"]]
print("\n7) Users older than 30 from Canada, Germany, and France:\n", first_world_users)


# =================================================================== String methods (startswith, endswith, contains)
# 8) Display the emails that start with the letter "a"
a_emails = users_df[users_df["email"].str.startswith("a")]
print("\n8) Emails starting with 'a':\n", a_emails)

# 9) Show the emails that end with the domain ".com"
dot_com_emails = users_df[users_df["email"].str.endswith(".com")]
print("\n9) Emails ending with '.com':\n", dot_com_emails)

# 10) Retrieve all the people whose name is Gabriel
name_contains_gabriel = users_df[users_df["name"].str.contains("Gabriel")]
print("\n10) People whose name contains 'Gabriel':\n", name_contains_gabriel)

# =================================================================== Grouping
# 11) Display the number of men and women in the dataset
genders = users_df.groupby("gender")["gender"].count()
print("\n11) Number of men and women in the dataset:\n", genders)

# 12) Display the country with the most women
country_with_more_women = (
    users_df[users_df["gender"] == "female"]
    .groupby("country")["country"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)
print("\n12) Country with the most women:\n", country_with_more_women)
