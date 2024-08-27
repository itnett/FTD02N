sql
CREATE TABLE PerformanceMetrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    cpu_usage DECIMAL(5, 2),
    memory_usage DECIMAL(5, 2),
    network_traffic DECIMAL(10, 2),
    disk_usage DECIMAL(5, 2),
    network_latency DECIMAL(5, 2)
);

CREATE TABLE Cubes (
    cube_id INT AUTO_INCREMENT PRIMARY KEY,
    length DECIMAL(5, 2)
);

CREATE TABLE RightTriangles (
    triangle_id INT AUTO_INCREMENT PRIMARY KEY,
    a DECIMAL(5, 2),
    b DECIMAL(5, 2)
);

CREATE TABLE Angles (
    angle_id INT AUTO_INCREMENT PRIMARY KEY,
    angle DECIMAL(5, 2)
);

CREATE TABLE Vectors (
    vector_id INT AUTO_INCREMENT PRIMARY KEY,
    x_component DECIMAL(5, 2),
    y_component DECIMAL(5, 2)
);

CREATE TABLE LinePoints (
    line_id INT AUTO_INCREMENT PRIMARY KEY,
    point1_x DECIMAL(5, 2),
    point1_y DECIMAL(5, 2),
    point2_x DECIMAL(5, 2),
    point2_y DECIMAL(5, 2)
);

CREATE TABLE PolynomialCoefficients (
    coeff_id INT AUTO_INCREMENT PRIMARY KEY,
    a DECIMAL(5, 2),
    b DECIMAL(5, 2),
    c DECIMAL(5, 2),
    x DECIMAL(5, 2)
);

CREATE TABLE ExponentialValues (
    exp_id INT AUTO_INCREMENT PRIMARY KEY,
    x DECIMAL(5, 2)
);

CREATE TABLE ObjectsInMotion (
    object_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2),
    acceleration DECIMAL(5, 2)
);

CREATE TABLE KineticEnergyCalculations (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2),
    velocity DECIMAL(5, 2)
);

CREATE TABLE PotentialEnergyCalculations (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2),
    height DECIMAL(5, 2)
);

CREATE TABLE DecimalValues (
    decimal_id INT AUTO_INCREMENT PRIMARY KEY,
    decimal_value INT
);

CREATE TABLE LinearEquations (
    equation_id INT AUTO_INCREMENT PRIMARY KEY,
    a1 DECIMAL(5,2),
    b1 DECIMAL(5,2),
    c1 DECIMAL(5,2),
    a2 DECIMAL(5,2),
    b2 DECIMAL(5,2),
    c2 DECIMAL(5,2)
);