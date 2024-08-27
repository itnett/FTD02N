-- Opprett en ny rolle og tilordne den til en bruker
CREATE ROLE 'data_analytiker';
GRANT SELECT ON bedrift.* TO 'data_analytiker';

-- Tilordne rollen til en bruker
GRANT 'data_analytiker' TO 'begrenset_bruker'@'localhost';