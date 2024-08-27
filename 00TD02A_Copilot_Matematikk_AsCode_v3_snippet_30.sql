-- Create the main database
CREATE DATABASE StudyProgram;

-- Use the database
USE StudyProgram;

-- Create a table for courses
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    topic VARCHAR(255),
    study_points DECIMAL(5, 2)
);

-- Insert sample data into Courses table
INSERT INTO Courses (course_name, topic, study_points) VALUES
('RealFaglige Redskap', 'Matematikk, Fysikk', 10),
('Yrkesrettet Kommunikasjon', 'Norsk, Engelsk', 10),
('LØM-emnet', 'Økonomistyring, Organisasjon og ledelse, Markedsføringsledelse', 10),
('IT-infrastruktur', 'IoT, Maskinvare og bruk av ITD-lab', 5),
('Cybersikkerhet', 'Cybersikkerhet', 5),
('Programmering', 'Programmering', 10),
('Nettverk 1', 'Nettverk 1', 5),
('Database', 'Database', 5),
('IT-sertifiseringer', 'CCNA, ITIL', 10),
('Serverdrift med Windows', 'Windows server, Virtualiseringsteknologi', 12.5),
('Nettverk 2', 'Nettverk 2, Nettverkssikkerhet', 10),
('Prosjektledelse', 'Prosjektledelse', 2.5),
('Serverdrift med Linux', 'Linux og container', 5),
('Monitorering og digital etterforskning', 'Monitorering, Digital etterforskning', 5),
('Skytjenester', 'Skytjenester', 5),
('Hovedprosjekt', 'Hovedprosjekt', 10);

-- Create a table for students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    enrollment_year INT
);

-- Insert sample data into Students table
INSERT INTO Students (student_name, enrollment_year) VALUES
('Student One', 2023),
('Student Two', 2023),
('Student Three', 2023);

-- Create a table for performance metrics
CREATE TABLE PerformanceMetrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    cpu_usage DECIMAL(5, 2),
    memory_usage DECIMAL(5, 2),
    network_traffic DECIMAL(10, 2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Insert sample data into PerformanceMetrics table
INSERT INTO PerformanceMetrics (student_id, course_id, cpu_usage, memory_usage, network_traffic) VALUES
(1, 1, 75.5, 60.2, 500.0),
(2, 1, 65.0, 55.5, 300.0),
(3, 1, 85.3, 70.1, 800.0);

-- Create a table for mathematics examples
CREATE TABLE MathematicsExamples (
    example_id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255),
    example TEXT
);

-- Insert sample data into MathematicsExamples table
INSERT INTO MathematicsExamples (topic, example) VALUES
('Regneregler', 'SELECT 5 + 3 * 2 AS result;'),
('Brøk og prosentregning', 'SELECT 50 / 100 * 20 AS result;'),
('Potenser', 'SELECT POWER(2, 3) AS result;'),
('Tall på standardform', 'SELECT 12345e-3 AS result;'),
('Sammentrekning og faktorisering', 'SELECT 12 * (3 + 2) AS result;'),
('Likninger og formelregning', 'SELECT (3 + 5) * 2 AS result;');

-- Create a table for physics examples
CREATE TABLE PhysicsExamples (
    example_id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255),
    example TEXT
);

-- Insert sample data into PhysicsExamples table
INSERT INTO PhysicsExamples (topic, example) VALUES
('SI-systemet', 'SELECT 1000 * 0.001 AS meters;'),
('Masse og massetetthet', 'SELECT 70 / 0.07 AS density;'),
('Usikkerhet', 'SELECT 100 * 1.05 AS upper_bound, 100 * 0.95 AS lower_bound;'),
('Kraft og bevegelse', 'SELECT 10 * 9.81 AS force;'),
('Energi', 'SELECT 0.5 * 10 * POWER(2, 2) AS kinetic_energy;');