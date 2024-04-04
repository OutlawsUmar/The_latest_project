from connect_db import Database
import admin_panel
import student_panel


def chek(query, status):
    email = input("Email: ")
    password = input("Password: ")

    data = Database.connect(query, "select")

    for i in data:
        if i[3] == email and i[4] == password:
            if status == "1":
                return admin_panel.admin(email, password)
            else:
                return student_panel.student(email, password)

        else:
            print("Password yoki Email noto'g'ri")
            return chek(query, status)


def login():
    print("Login Page")
    status = input("""
        1. Admin
        2. Student
            >>> """)

    if status == "1":
        query = """SELECT * FROM mentor"""
        return chek(query, status)


    elif status == "2":
        query = """SELECT * FROM student"""
        return chek(query, status)

    else:
        print("Error")
        return login()


