sql
-- Example table for assignment times
CREATE TABLE AssignmentTimes (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    num_tasks INT,
    avg_time_per_task DECIMAL(5, 2) -- in hours
);

-- Insert sample data into AssignmentTimes
INSERT INTO AssignmentTimes (student_id, num_tasks, avg_time_per_task) VALUES
(1, 10, 1.5),
(2, 8, 2.0),
(3, 12, 1.2);

-- Calculate total time spent by each student
SELECT student_id, 
       num_tasks * avg_time_per_task AS total_time 
FROM AssignmentTimes;