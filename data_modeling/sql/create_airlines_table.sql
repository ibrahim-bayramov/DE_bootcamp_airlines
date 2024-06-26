-- Create table to store airline data
CREATE TABLE IF NOT EXISTS airlines (
    airline_id VARCHAR(10) PRIMARY KEY,
    airline_id_icao VARCHAR(10),
    name VARCHAR(255)
);