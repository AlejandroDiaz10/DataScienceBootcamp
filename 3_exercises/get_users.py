# https://gist.github.com/eduardogpg/dfacf1da624b5e9fa321f8d809f7ab26

import csv
import requests

URL = "https://randomuser.me/api/?results=2000"

if __name__ == "__main__":

    response = requests.get(URL)
    if response.status_code == 200:

        payload = response.json()
        users = payload.get("results")

        with open("users.csv", "w") as user_file:
            writer = csv.writer(user_file, delimiter=",")
            writer.writerow(
                ["name", "age", "username", "email", "country", "postcode", "gender"]
            )

            for user in users:
                name = user.get("name")
                name = "{title} {first} {last}".format(**name)

                country = user.get("location")["country"]
                postcode = user.get("location")["postcode"]

                email = user.get("email")
                age = user.get("dob")["age"]
                username = user.get("login")["username"]

                gender = user.get("gender")

                writer.writerow([name, age, username, email, country, postcode, gender])
