-- Create the main database
CREATE DATABASE StudyProgram;

-- Use the database
USE StudyProgram;

-- Create table for courses
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(10),
    course_name VARCHAR(255),
    topic VARCHAR(255),
    study_points DECIMAL(5, 2),
    start_semester VARCHAR(10)
);

-- Create table for students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    enrollment_year INT
);

-- Create table for performance metrics
CREATE TABLE PerformanceMetrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    cpu_usage DECIMAL(5, 2),
    memory_usage DECIMAL(5, 2),
    network_traffic DECIMAL(10, 2),
    disk_usage DECIMAL(5, 2),
    network_latency DECIMAL(5, 2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for course content
CREATE TABLE CourseContent (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    topic VARCHAR(255),
    description TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for learning outcomes
CREATE TABLE LearningOutcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    category VARCHAR(255),
    description TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for assignments
CREATE TABLE Assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    title VARCHAR(255),
    description TEXT,
    due_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for student submissions
CREATE TABLE StudentSubmissions (
    submission_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT,
    student_id INT,
    submission_date DATE,
    grade VARCHAR(10),
    feedback TEXT,
    FOREIGN KEY (assignment_id) REFERENCES Assignments(assignment_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Create table for class attendance
CREATE TABLE ClassAttendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    date DATE,
    status VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for projects
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    project_name VARCHAR(255),
    description TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for resources
CREATE TABLE Resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    resource_name VARCHAR(255),
    type VARCHAR(50),
    link TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create table for feedback
CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    date DATE,
    feedback TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);