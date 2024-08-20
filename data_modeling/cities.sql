CREATE TABLE IF NOT EXISTS cities (
    city_code                VARCHAR(3) NOT NULL PRIMARY KEY,
    country_code             VARCHAR(2) NOT NULL,
    city_name                VARCHAR(50) NOT NULL,
    utc_offset               VARCHAR(6) NOT NULL,
    time_zone_id             VARCHAR(19)
);