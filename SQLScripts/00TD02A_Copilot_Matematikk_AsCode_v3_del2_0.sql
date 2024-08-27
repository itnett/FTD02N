sql
-- Example table for virtual lab costs
CREATE TABLE VirtualLabCosts (
    cost_id INT AUTO_INCREMENT PRIMARY KEY,
    lab_type VARCHAR(255),
    estimated_time DECIMAL(5, 2), -- in hours
    hourly_rate DECIMAL(5, 2), -- in currency unit
    hardware_cost DECIMAL(10, 2), -- in currency unit
    service_cost DECIMAL(10, 2) -- in currency unit
);

-- Insert sample data into VirtualLabCosts
INSERT INTO VirtualLabCosts (lab_type, estimated_time, hourly_rate, hardware_cost, service_cost) VALUES
('Docker', 20, 50, 0, 100),
('VirtualBox', 25, 50, 0, 150),
('GNS3', 30, 50, 0, 200),
('Cisco Hardware', 0, 0, 10000, 0),
('Kubernetes AWS', 15, 50, 0, 500),
('Kubernetes Azure', 15, 50, 0, 450);

-- Calculate total cost for each lab type
SELECT lab_type, 
       estimated_time * hourly_rate + hardware_cost + service_cost AS total_cost 
FROM VirtualLabCosts;