sql
   EXPLAIN SELECT s.name, c.course_name
   FROM students s
   JOIN enrollments e ON s.student_id = e.student_id
   JOIN courses c ON e.course_id = c.course_id
   WHERE c.course_name = 'Database Systems';