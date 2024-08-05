-- Create table to store aircraft data
CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255),
    airline_equip_code VARCHAR(10),
    names_id INT FOREIGN KEY
);