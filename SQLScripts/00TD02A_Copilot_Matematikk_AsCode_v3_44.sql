sql
-- Import Experiments data
LOAD DATA INFILE 'experiments.csv'
INTO TABLE Experiments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(experiment_id, experiment_name, description, date);

-- Import Assignments data
LOAD DATA INFILE 'assignments.csv'
INTO TABLE Assignments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(assignment_id, course_id, student_id, title, description, due_date);

-- Import Labs data
LOAD DATA INFILE 'labs.csv'
INTO TABLE Labs
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(lab_id, lab_name, description, date);

-- Import Exercises data
LOAD DATA INFILE 'exercises.csv'
INTO TABLE Exercises
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(exercise_id, exercise_name, description, date);

-- Import SecurityAnalyses data
LOAD DATA INFILE 'security_analyses.csv'
INTO TABLE SecurityAnalyses
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(analysis_id, analysis_name, description, date, results);

-- Import SWOTAnalyses data
LOAD DATA INFILE 'swot_analyses.csv'
INTO TABLE SWOTAnalyses
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(swot_id, analysis_name, strengths, weaknesses, opportunities, threats, date);