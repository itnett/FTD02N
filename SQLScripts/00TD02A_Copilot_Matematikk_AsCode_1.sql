sql
CREATE DATABASE Geometry;

USE Geometry;

CREATE TABLE Spheres (
    id INT AUTO_INCREMENT,
    radius DECIMAL(5,2),
    volume DECIMAL(8,2),
    PRIMARY KEY (id)
);

CREATE TABLE Quadratics (
    id INT AUTO_INCREMENT,
    a DECIMAL(5,2),
    b DECIMAL(5,2),
    c DECIMAL(5,2),
    root1 DECIMAL(5,2),
    root2 DECIMAL(5,2),
    PRIMARY KEY (id)
);

INSERT INTO Spheres (radius, volume) VALUES (5, 523.6);
INSERT INTO Quadratics (a, b, c, root1, root2) VALUES (1, -3, 2, 2, 1);