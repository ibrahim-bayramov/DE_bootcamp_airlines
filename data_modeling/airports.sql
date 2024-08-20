CREATE TABLE IF NOT EXISTS airports (
    airport_code                 VARCHAR(3) NOT NULL PRIMARY KEY,
    latitude                     NUMERIC(8,4) NOT NULL,
    longitude                    NUMERIC(8,4) NOT NULL,
    city_code                    VARCHAR(3) NOT NULL,
    country_code                 VARCHAR(2) NOT NULL,
    location_type                VARCHAR(7) NOT NULL,
    airport_name                 VARCHAR(50) NOT NULL,
    utc_offset                   VARCHAR(6),
    time_zone_id                 VARCHAR(50)
);