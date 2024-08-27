CREATE TABLE compliance_check (
    id SERIAL PRIMARY KEY,
    regulation VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE corrective_action (
    id SERIAL PRIMARY KEY,
    compliance_check_id INT REFERENCES compliance_check(id),
    action VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    implemented_at TIMESTAMP
);