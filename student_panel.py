from connect_db import Database


def courses(email, password):
    query = "SELECT * FROM course"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
            ID: {i[0]}
            Name: {i[1]}
            Description: {i[2]}
            Price: {i[7]}
            Rating: {i[3]}
        """)

    back = input("""
        0. back
            >>> """)
    if back == "0":
        return student(email, password)

    else:
        print("Error")
        return courses(email, password)


def speciality(email, password):
    query = "SELECT * FROM speciality"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
            ID: {i[0]}
            Name: {i[1]}
        """)

    back = input("""
        0. back
            >>> """)
    if back == "0":
        return student(email, password)

    else:
        print("Error")
        return speciality(email, password)

def student(email, password):
    print("Student Page")
    services = input("""
        1. Specialitys
        2. Courses
        3. Profile
        4. Log Out
            >>> """)

    if services == "1":
        return speciality(email, password)

    elif services == "2":
        return courses(email, password)

    elif services == "3":
        pass

    elif services == "4":
        pass

    else:
        return student(email, password)