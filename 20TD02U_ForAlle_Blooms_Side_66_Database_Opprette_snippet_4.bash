# Opprett en RDS MySQL-instans på AWS (forutsetter at AWS CLI er satt opp)
aws rds create-db-instance \
    --db-instance-identifier mydatabase \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username admin \
    --master-user-password passord123 \
    --backup-retention-period 7

# Logg inn på RDS-databasen når den er opprettet
mysql -h mydatabase.xxxxxxxxxxxx.us-west-2.rds.amazonaws.com -u admin -p

# Opprett en database
CREATE DATABASE skyprosjekt;

# Bruk databasen
USE skyprosjekt;

# Opprett en tabell
CREATE TABLE brukere (
    bruker_id INT PRIMARY KEY AUTO_INCREMENT,
    brukernavn VARCHAR(50),
    epost VARCHAR(100)
);

# Sett inn data i tabellen
INSERT INTO brukere (brukernavn, epost) VALUES ('admin', 'admin@example.com');

# Sjekk innholdet i tabellen
SELECT * FROM brukere;