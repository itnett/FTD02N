sql
-- Import Courses data
LOAD DATA INFILE 'courses.csv'
INTO TABLE Courses
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(course_id, course_name, topic, study_points);

-- Import Students data
LOAD DATA INFILE 'students.csv'
INTO TABLE Students
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(student_id, student_name, enrollment_year);

-- Import PerformanceMetrics data
LOAD DATA INFILE 'performance_metrics.csv'
INTO TABLE PerformanceMetrics
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(metric_id, student_id, course_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency

);

-- Import MathematicsExamples data
LOAD DATA INFILE 'mathematics_examples.csv'
INTO TABLE MathematicsExamples
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(example_id, topic, example);

-- Import PhysicsExamples data
LOAD DATA INFILE 'physics_examples.csv'
INTO TABLE PhysicsExamples
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(example_id, topic, example);

-- Import CyberSecurityExamples data
LOAD DATA INFILE 'cyber_security_examples.csv'
INTO TABLE CyberSecurityExamples
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(example_id, topic, example);