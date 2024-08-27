-- Create the main database
CREATE DATABASE StudyProgram;

-- Use the database
USE StudyProgram;

-- Create table for programming topics
CREATE TABLE ProgrammingTopics (
    topic_id INT AUTO_INCREMENT PRIMARY KEY,
    topic_name VARCHAR(255),
    description TEXT
);

-- Create table for learning outcomes
CREATE TABLE LearningOutcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255),
    description TEXT
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
    date DATE,
    status VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Create table for projects
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255),
    description TEXT,
    start_date DATE,
    end_date DATE
);

-- Create table for resources
CREATE TABLE Resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_name VARCHAR(255),
    type VARCHAR(50),
    link TEXT
);

-- Create table for feedback
CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    feedback TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);