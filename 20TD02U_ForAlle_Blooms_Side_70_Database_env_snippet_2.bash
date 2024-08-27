# Installere PostgreSQL server
        sudo apt update
        sudo apt install postgresql postgresql-contrib

        # Starte PostgreSQL server
        sudo systemctl start postgresql

        # Stoppe PostgreSQL server
        sudo systemctl stop postgresql

        # Logge inn på PostgreSQL server
        sudo -u postgres psql