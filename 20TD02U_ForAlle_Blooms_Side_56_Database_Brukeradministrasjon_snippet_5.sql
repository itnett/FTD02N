-- Opprette en kompleks rollehierarki i PostgreSQL
CREATE ROLE admin_role;
CREATE ROLE editor_role;
CREATE ROLE viewer_role;

-- Gi spesifikke rettigheter til hver rolle
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin_role;
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO editor_role;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO viewer_role;

-- Tilordne roller til brukere
GRANT admin_role TO admin_user;
GRANT editor_role TO editor_user;
GRANT viewer_role TO viewer_user;