sql
-- Data for PerformanceMetrics
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency) VALUES
(1, 75.5, 60.2, 500.0, 250.0, 20.5),
(2, 65.0, 55.5, 300.0, 200.0, 15.3),
(3, 85.3, 70.1, 800.0, 300.0, 25.8);

-- Data for Cubes
INSERT INTO Cubes (length) VALUES
(3.0),
(4.5),
(2.1);

-- Data for RightTriangles
INSERT INTO RightTriangles (a, b) VALUES
(3.0, 4.0),
(5.0, 12.0);

-- Data for Angles
INSERT INTO Angles (angle) VALUES
(30),
(45),
(60);

-- Data for Vectors
INSERT INTO Vectors (x_component, y_component) VALUES
(3.0, 4.0),
(5.0, 12.0);

-- Data for LinePoints
INSERT INTO LinePoints (point1_x, point1_y, point2_x, point2_y) VALUES
(1, 2, 3, 4),
(2, 3, 4, 5);

-- Data for PolynomialCoefficients
INSERT INTO PolynomialCoefficients (a, b, c, x) VALUES
(1, 2, 3, 4),
(2, -1, 0, 3);

-- Data for ExponentialValues
INSERT INTO ExponentialValues (x) VALUES
(1),
(2),
(3);

-- Data for ObjectsInMotion
INSERT INTO ObjectsInMotion (mass, acceleration) VALUES
(10, 9.81),
(5, 3.5);

-- Data for KineticEnergyCalculations
INSERT INTO KineticEnergyCalculations (mass, velocity) VALUES
(10, 15),
(5, 20);

-- Data for PotentialEnergyCalculations
INSERT INTO PotentialEnergyCalculations (mass, height) VALUES
(10, 10),
(5, 20);

-- Data for DecimalValues
INSERT INTO DecimalValues (decimal_value) VALUES
(10),
(15),
(255);

-- Data for LinearEquations
INSERT INTO LinearEquations (a1, b1, c1, a2, b2, c2) VALUES
(2, 3, 5, 4, -1, 3),
(1, 2, 3, 2, 1, 4);