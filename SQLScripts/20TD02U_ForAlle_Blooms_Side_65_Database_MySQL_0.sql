sql
-- Opprett en ny bruker med begrensede rettigheter
CREATE USER 'begrenset_bruker'@'localhost' IDENTIFIED BY 'SterktPassord!123';
GRANT SELECT, INSERT ON bedrift.* TO 'begrenset_bruker'@'localhost';