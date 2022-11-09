from random import randint
import random
import sqlite3
import faker


fake_data = faker.Faker()

GROUP_NUM = 3
OBJECT_NUM = 5
TEACHER_NUM = 3
STUDENTS_NUM = 30
RETING_NUM = 12
RATING_OBJ_NUM = 4


def create_bd():
    with open("create_table.sql", "r") as file:
        sql_create = file.read()

    with sqlite3.connect("homework.db") as con:
        cur = con.cursor()
        cur.executescript(sql_create)


def generate_table(group_num, objects_num, teacher_num, students_num, reting_num, rating_obj_num):
    group_list = []
    for _ in range(0, group_num):
        group_list.append((fake_data.company(),))
    
    objects_list = []
    for _ in range(0, objects_num):
        objects_list.append((fake_data.job(), randint(1, TEACHER_NUM)))

    teacher_list = []
    for _ in range(0, teacher_num):
        fake_name = fake_data.name()
        fake_name = fake_name.split()
        teacher_list.append((fake_name[0], fake_name[1]))

    students_list = []
    for _ in range(0, students_num):
        fake_name = fake_data.name()
        fake_name = fake_name.split()
        students_list.append((fake_name[0], fake_name[1]))
    
    rating_list = []

    for rating in range(1, reting_num + 1):
        rating_list.append((rating,))

    students_table_list = []
    for stud_id in range(1, len(students_list) + 1):
        students_table_list.append((stud_id, randint(1, len(group_list))))

    rating_stud_list = []
    for stud_id in range(1, len(students_list) + 1):

        object_rand = randint(1, len(objects_list))
        object_rand_list = random.sample(list(range(1, 6)), object_rand)

        for object_id in object_rand_list:
            for _ in range(1, rating_obj_num + 1):
                rating_stud_list.append((stud_id, object_id, randint(1, len(rating_list))))
    
    return students_list, teacher_list, objects_list, group_list, rating_list, students_table_list, rating_stud_list


def add_to_bd(students_list, teacher_list, objects_list, group_list, rating_list, students_table_list, rating_stud_list):
    with sqlite3.connect("homework.db   ") as con:
        cur = con.cursor()

        add_gruop_table = """INSERT INTO groups(group_name) VALUES(?)"""
        cur.executemany(add_gruop_table, group_list)

        add_stud_list_table = """INSERT INTO students_info(name, surname) VALUES(?, ?)"""
        cur.executemany(add_stud_list_table, students_list)

        add_objects_table = """INSERT INTO objects(object_name, teacher_id) VALUES(?, ?)"""
        cur.executemany(add_objects_table, objects_list)

        add_teacher_table = """INSERT INTO teacher_info(name, surname) VALUES(?, ?)""" 
        cur.executemany(add_teacher_table, teacher_list)

        add_reting_table = """INSERT INTO ratings(rating_int) VALUES(?)"""
        cur.executemany(add_reting_table, rating_list)

        add_students_table = """INSERT INTO students(student_id, group_id) VALUES(?, ?)"""
        cur.executemany(add_students_table, students_table_list)

        add_rating_students_table = """INSERT INTO rating_students(student_id, object_id, rating_id) VALUES(?, ?, ?)"""
        cur.executemany(add_rating_students_table, rating_stud_list)


if __name__ == "__main__":
    create_bd()
    students_list, teacher_list, objects_list, group_list, rating_list, students_table_list, rating_stud_list = generate_table(GROUP_NUM, OBJECT_NUM, TEACHER_NUM, STUDENTS_NUM, RETING_NUM, RATING_OBJ_NUM)  
    add_to_bd(students_list, teacher_list, objects_list, group_list, rating_list, students_table_list, rating_stud_list)