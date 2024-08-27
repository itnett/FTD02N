sql
   USE skole;
   CREATE TABLE elever (
       elev_id INT AUTO_INCREMENT PRIMARY KEY,
       navn VARCHAR(100),
       fødselsdato DATE
   );
   CREATE TABLE kurs (
       kurs_id INT AUTO_INCREMENT PRIMARY KEY,
       kursnavn VARCHAR(100)
   );
   CREATE TABLE påmelding (
       påmelding_id INT AUTO_INCREMENT PRIMARY KEY,
       elev_id INT,
       kurs_id INT,
       FOREIGN KEY (elev_id) REFERENCES elever(elev_id),
       FOREIGN KEY (kurs_id) REFERENCES kurs(kurs_id)
   );