CREATE LOGIN testuser WITH PASSWORD = 'TestPassword123!';
     CREATE USER testuser FOR LOGIN testuser;
     ALTER ROLE db_datareader ADD MEMBER testuser;
     ALTER ROLE db_datawriter ADD MEMBER testuser;