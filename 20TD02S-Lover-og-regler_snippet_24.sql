CREATE USER compliance_user WITH PASSWORD 'securePassword';
GRANT SELECT, INSERT, UPDATE ON compliance_check TO compliance_user;
GRANT SELECT, INSERT, UPDATE ON corrective_action TO compliance_user;