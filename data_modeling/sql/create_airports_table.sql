-- Create table to store airport data
CREATE TABLE IF NOT EXISTS airports (
    airport_code VARCHAR(10) PRIMARY KEY,
    latitude NUMERIC(10, 7),
    longitude NUMERIC(10, 7),
    city_code VARCHAR(10),
    country_code VARCHAR(2),
    location_type VARCHAR(50),
    name VARCHAR(255),
    utc_offset VARCHAR(10),
    timezone_id VARCHAR(50)
);
