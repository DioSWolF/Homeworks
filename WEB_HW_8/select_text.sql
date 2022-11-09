-- ~~~~~~~~~~~~~~ 1
SELECT student_id, si.name, si.surname, AVG(rating_id) FROM rating_students rs
JOIN objects o ON object_id = o.id 
JOIN students_info si ON student_id = si.id 
GROUP BY student_id 
ORDER BY AVG(rating_id) DESC  LIMIT 5

-- ~~~~~~~~~~~~~~ 2
SELECT student_id, si.name, si.surname, rating_id, object_id FROM rating_students rs
JOIN objects o ON object_id = o.id 
JOIN students_info si ON student_id = si.id 
GROUP BY object_id
ORDER BY student_id, MAX(rating_id) 

-- ~~~~~~~~~~~~~~ 3
SELECT g.group_name, o.object_name, AVG(rs.rating_id) FROM rating_students rs 
JOIN students s ON rs.student_id = s.id 
JOIN objects o ON rs.object_id = o.id 
JOIN groups g ON s.group_id = g.id 
GROUP BY o.object_name, s.group_id
ORDER BY s.group_id

-- ~~~~~~~~~~~~~~ 4
SELECT AVG(rating_id) FROM rating_students rs 

-- ~~~~~~~~~~~~~~ 5
SELECT ti.name, ti.surname, o.object_name FROM objects o 
JOIN teacher_info ti ON ti.id = o.teacher_id 
ORDER BY o.teacher_id 

-- ~~~~~~~~~~~~~~ 6
SELECT g.group_name, s.student_id, si.name, si.surname FROM students s 
JOIN students_info si ON si.id = s.id 
JOIN groups g ON g.id = s.group_id 
ORDER BY group_id 

-- ~~~~~~~~~~~~~~ 7
SELECT rs.student_id, si.name, si.surname, g.group_name, o.object_name, rs.rating_id FROM rating_students rs 
JOIN students s ON rs.student_id = s.student_id
JOIN students_info si ON s.student_id = si.id
JOIN groups g ON s.group_id = g.id 
JOIN objects o ON o.id = rs.object_id 
ORDER BY g.group_name, object_id 

-- ~~~~~~~~~~~~~~ 8


-- ~~~~~~~~~~~~~~ 9
SELECT student_id, si.name, si.surname, o.object_name FROM rating_students rs 
JOIN objects o ON object_id = o.id 
JOIN students_info si ON student_id = si.id 
WHERE student_id = 1
GROUP BY o.object_name 

-- ~~~~~~~~~~~~~~ 10
SELECT o.teacher_id, ti.name, ti.surname, student_id, si.name, si.surname, o.object_name FROM rating_students rs 
JOIN objects o ON object_id = o.id JOIN teacher_info ti ON o.teacher_id  = ti.id 
JOIN students_info si ON student_id = si.id 
WHERE o.teacher_id = 1 AND student_id = 2
GROUP BY o.object_name 

-- ~~~~~~~~~~~~~~ 11
SELECT o.teacher_id, ti.name, ti.surname, si.id, si.name, si.surname, AVG(rating_id) FROM rating_students rs 
JOIN objects o ON object_id = o.id 
JOIN teacher_info ti ON o.teacher_id  = ti.id 
JOIN students_info si ON si.id = rs.student_id 
GROUP BY o.teacher_id, student_id

-- ~~~~~~~~~~~~~~ 12
SELECT o.teacher_id, ti.name, ti.surname, AVG(rating_id) FROM rating_students rs 
JOIN objects o ON object_id = o.id JOIN teacher_info ti ON o.teacher_id  = ti.id 
GROUP BY o.teacher_id 

