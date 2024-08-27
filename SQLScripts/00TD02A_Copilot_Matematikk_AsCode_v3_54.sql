sql
-- Import ProgrammingTopics data
LOAD DATA INFILE 'programming_topics.csv'
INTO TABLE ProgrammingTopics
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(topic_id, topic_name, description);

-- Import LearningOutcomes data
LOAD DATA INFILE 'learning_outcomes.csv'
INTO TABLE LearningOutcomes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(outcome_id, category, description);

-- Import Assignments data
LOAD DATA INFILE 'assignments.csv'
INTO TABLE Assignments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(assignment_id, course_id, title, description, due_date);

-- Import StudentSubmissions data
LOAD DATA INFILE 'student_submissions.csv'
INTO TABLE StudentSubmissions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(submission_id, assignment_id, student_id, submission_date, grade, feedback);

-- Import ClassAttendance data
LOAD DATA INFILE 'class_attendance.csv'
INTO TABLE ClassAttendance
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(attendance_id, student_id, date, status);

-- Import Projects data
LOAD DATA INFILE 'projects.csv'
INTO TABLE Projects
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(project_id, project_name, description, start_date, end_date);

-- Import Resources data
LOAD DATA INFILE 'resources.csv'
INTO TABLE Resources
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(resource_id, resource_name, type, link);

-- Import Feedback data
LOAD DATA INFILE 'feedback.csv'
INTO TABLE Feedback
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(feedback_id, student_id, date, feedback);