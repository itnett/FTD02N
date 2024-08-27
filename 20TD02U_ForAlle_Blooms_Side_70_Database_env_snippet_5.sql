-- Opprette en bruker
        CREATE USER ny_bruker WITH PASSWORD 'passord';

        -- Gi brukeren tilgang til en database
        GRANT ALL PRIVILEGES ON DATABASE min_database TO ny_bruker;

        -- Sikkerhetskopiere en database
        pg_dump -U postgres min_database > min_database_backup.sql

        -- Gjenopprette en database fra sikkerhetskopi
        psql -U postgres -d min_database -f min_database_backup.sql