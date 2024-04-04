from connect_db import Database
import login


def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")

    bio = input("Bio: ")
    headline = input("Headline: ")
    # status = input("Student or Mentor: ")
    query = ""
    # if status.lower() == "student":
    query = f"""INSERT INTO student(first_name, last_name, email, password, bio, headline)
            VALUES('{first_name}', '{last_name}', '{email}', '{password_1}', '{bio}', '{headline}')"""


    print(Database.connect(query, "insert"))
    return login.login()




