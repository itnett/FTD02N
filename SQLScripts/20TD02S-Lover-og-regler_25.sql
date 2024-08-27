sql
CREATE TABLE log_entries (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    action VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);