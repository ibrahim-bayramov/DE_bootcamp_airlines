CREATE TABLE IF NOT EXISTS cities (
    city_code VARCHAR(10) PRIMARY KEY,
    country_code VARCHAR(2),
    utc_offset VARCHAR(10),
    timezone_id VARCHAR(50),
    names JSONB,
    airports JSONB,
    meta JSONB
);
