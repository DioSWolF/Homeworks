CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    group_name VARCHAR(64)
);

CREATE TABLE students_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name VARCHAR(64),
    surname VARCHAR(64)
);

CREATE TABLE teacher_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name VARCHAR(64),
    surname VARCHAR(64)
);

CREATE TABLE ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    rating_int INT UNSIGNED
);

CREATE TABLE objects (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    object_name VARCHAR(128),
    teacher_id INT UNSIGNED,

    FOREIGN KEY (teacher_id) REFERENCES teacher_info (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE   
);

CREATE TABLE students ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    student_id INT,
    group_id INT UNSIGNED,

    FOREIGN KEY (student_id) REFERENCES students_info (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
    FOREIGN KEY (group_id) REFERENCES groups (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE rating_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    student_id INT UNSIGNED,
    object_id INT UNSIGNED, 
    rating_id INT UNSIGNED, 
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (student_id) REFERENCES students (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE   
    FOREIGN KEY (object_id) REFERENCES objects (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE   
    FOREIGN KEY (rating_id) REFERENCES ratings (id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE   
);
