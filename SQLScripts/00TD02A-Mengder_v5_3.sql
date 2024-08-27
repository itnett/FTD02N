sql
CREATE TABLE Person (
    PersonID INT PRIMARY KEY,
    Navn VARCHAR(50),
    Alder INT,
    Kjønn VARCHAR(10),
    Vekt FLOAT
);

CREATE TABLE Koffert (
    KoffertID INT PRIMARY KEY,
    Type VARCHAR(20),
    Vekt FLOAT,
    PersonID INT,
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

CREATE TABLE Alkohol (
    AlkoholID INT PRIMARY KEY,
    Type VARCHAR(20),
    Mengde FLOAT,
    PersonID INT,
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

CREATE TABLE Faktor (
    FaktorID INT PRIMARY KEY,
    Type VARCHAR(20),
    Verdi VARCHAR(50),
    PersonID INT,
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);