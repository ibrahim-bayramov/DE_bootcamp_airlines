CREATE TABLE IF NOT EXISTS airports (
    airport_code                 VARCHAR(3) NOT NULL PRIMARY KEY,
    position_coordinate_latitude  NUMERIC(8,4) NOT NULL,
    position_coordinate_longitude NUMERIC(8,4) NOT NULL,
    airport_name                 VARCHAR(20) NOT NULL,
    city_code                    VARCHAR(3) NOT NULL,
    country_code                 VARCHAR(2) NOT NULL,
    location_type                VARCHAR(7) NOT NULL
);