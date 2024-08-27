-- Opprette en rolle i PostgreSQL
CREATE ROLE read_only;

-- Gi rollen read-only tilgang til alle tabeller i en database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only;

-- Tilordne rollen til en bruker
GRANT read_only TO student;