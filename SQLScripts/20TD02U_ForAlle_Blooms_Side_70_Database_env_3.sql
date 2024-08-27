sql
        -- Opprette en bruker
        CREATE USER 'ny_bruker'@'localhost' IDENTIFIED BY 'passord';

        -- Gi brukeren tilgang til en database
        GRANT ALL PRIVILEGES ON min_database.* TO 'ny_bruker'@'localhost';

        -- Sikkerhetskopiere en database
        mysqldump -u root -p min_database > min_database_backup.sql

        -- Gjenopprette en database fra sikkerhetskopi
        mysql -u root -p min_database < min_database_backup.sql