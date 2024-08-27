sql
-- Create the main database
CREATE DATABASE StudyProgram;

-- Use the database
USE StudyProgram;

-- Create tables for courses
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    topic VARCHAR(255),
    study_points DECIMAL(5, 2)
);

-- Create tables for students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    enrollment_year INT
);

-- Create tables for performance metrics
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

-- Create tables for mathematics examples
CREATE TABLE MathematicsExamples (
    example_id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255),
    example TEXT
);

-- Create tables for physics examples
CREATE TABLE PhysicsExamples (
    example_id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255),
    example TEXT
);

-- Create tables for cybersecurity examples
CREATE TABLE CyberSecurityExamples (
    example_id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255),
    example TEXT
);

-- Create tables for experiments and labs
CREATE TABLE Experiments (
    experiment_id INT AUTO_INCREMENT PRIMARY KEY,
    experiment_name VARCHAR(255),
    description TEXT,
    date DATE
);

CREATE TABLE Assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    student_id INT,
    title VARCHAR(255),
    description TEXT,
    due_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

CREATE TABLE Labs (
    lab_id INT AUTO_INCREMENT PRIMARY KEY,
    lab_name VARCHAR(255),
    description TEXT,
    date DATE
);

CREATE TABLE Exercises (
    exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    exercise_name VARCHAR(255),
    description TEXT,
    date DATE
);

-- Create tables for security analyses
CREATE TABLE SecurityAnalyses (
    analysis_id INT AUTO_INCREMENT PRIMARY KEY,
    analysis_name VARCHAR(255),
    description TEXT,
    date DATE,
    results TEXT
);

-- Create tables for SWOT analyses
CREATE TABLE SWOTAnalyses (
    swot_id INT AUTO_INCREMENT PRIMARY KEY,
    analysis_name VARCHAR(255),
    strengths TEXT,
    weaknesses TEXT,
    opportunities TEXT,
    threats TEXT,
    date DATE
);