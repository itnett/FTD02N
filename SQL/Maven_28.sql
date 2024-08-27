sql
     CREATE TABLE Bruker (
         bruker_id INT PRIMARY KEY AUTO_INCREMENT,
         brukernavn VARCHAR(50) NOT NULL,
         passord_hash VARCHAR(64) NOT NULL
     );

     INSERT INTO Bruker (brukernavn, passord_hash)
     VALUES ('admin', SHA2('passord123', 256));