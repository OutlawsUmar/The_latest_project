from connect_db import Database
from classes import Speciality, Course


def back(email, password):
    back = input("""
            0. back
                >>> """)
    if back == "0":
        return admin(email, password)

    else:
        print("Error")
        return course(email, password)

def course_insert(email, password):

    name = input("Name: ")
    description = input("description: ")
    rating = input("rating: ")
    active_Students = input("active_Students: ")
    mentor_id = input("mentor_id: ")
    lenguage_id = input("lenguage_id: ")
    price = input("price: ")
    course_status_id = input("course_status_id: ")
    support_date = input("support_date: ")
    spec = Course(name, description, rating, active_Students, mentor_id, lenguage_id, price, course_status_id, support_date)
    print(spec.insert("course"))
    return back(email, password)

def course_list(email, password):
    data = Course.select("course")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
                description: {i[2]}
                rating: {i[3]}
                Mentor First Name: {i[4]}
                Mentor Last Name: : {i[5]}
                Status: {i[6]}
                Lenguage: {i[7]}
                Price: {i[8]}
                            """)

    return back(email, password)

def course_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Course.update_id("course", column_name, old_data, new_data))
    else:
        print(Course.update("course", column_name, old_data, new_data))
    return course(email, password)


def course_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "speciality_id":
        print(Course.delete_id("course", column_name, data))

    else:
        print(Course.delete("course", column_name, data))

    return course(email, password)


def course(email, password):
    services = input("""
            1. List
            2. Insert
            3. Update
            4. Delete
            0. back
                >>> """)

    if services == "1":
        return course_list(email, password)

    elif services == "2":
        return course_insert(email, password)

    elif services == "3":
        return course_update(email, password)

    elif services == "4":
        return course_delete(email, password)

def speciality_insert(email, password):

    name = input("Name: ")
    spec = Speciality(name)
    print(spec.insert("speciality"))
    return back(email, password)

def speciality_list(email, password):
    data = Speciality.select("speciality")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)

    return back(email, password)

def speciality_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Speciality.update_id("speciality", column_name, old_data, new_data))
    else:
        print(Speciality.update("speciality", column_name, old_data, new_data))
    return speciality(email, password)


def speciality_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "speciality_id":
        print(Speciality.delete_id("speciality", column_name, data))

    else:
        print(Speciality.delete("speciality", column_name, data))

    return speciality(email, password)


def speciality(email, password):
    services = input("""
            1. List
            2. Insert
            3. Update
            4. Delete
            0. back
                >>> """)

    if services == "1":
        return speciality_list(email, password)

    elif services == "2":
        return speciality_insert(email, password)

    elif services == "3":
        return speciality_update(email, password)

    elif services == "4":
        return speciality_delete(email, password)

    elif services == "0":
        return admin(email, password)

    else:
        return speciality(email, password)

def admin(email, password):
    print("Admin Page")
    services = input("""
        1. Specialities
        2. Courses
        3. Profile
        4. Log Out
            >>> """)

    if services == "1":
        return speciality(email, password)

    elif services == "2":
        return course(email, password)

    elif services == "3":
        pass

    elif services == "4":
        pass

    else:
        return admin(email, password)