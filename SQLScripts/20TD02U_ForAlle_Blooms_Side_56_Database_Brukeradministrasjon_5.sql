sql
-- Hente en liste over alle brukere og deres rettigheter i PostgreSQL
SELECT grantee, privilege_type, table_name
FROM information_schema.role_table_grants
WHERE grantee != 'pg_database_owner';

-- Identifisere brukere med potensielt farlige rettigheter
SELECT rolname FROM pg_roles WHERE rolsuper = true;