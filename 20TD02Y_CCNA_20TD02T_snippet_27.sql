USE studentdb;

   CREATE TABLE students (
       student_id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100) UNIQUE
   );

   CREATE TABLE courses (
       course_id INT AUTO_INCREMENT PRIMARY KEY,
       course_name VARCHAR(100),
       course_code VARCHAR(10) UNIQUE
   );

   CREATE TABLE enrollments (
       enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
       student_id INT,
       course_id INT,
       FOREIGN KEY (student_id) REFERENCES students(student_id),
       FOREIGN KEY (course_id) REFERENCES courses(course_id)
   );