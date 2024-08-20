CREATE TABLE IF NOT EXISTS airlines (
    airline_id             VARCHAR(2) NOT NULL PRIMARY KEY,
    airline_id_icao        VARCHAR(3),
    airlines_language_code VARCHAR(2) NOT NULL,
    airlines_name          VARCHAR(41) NOT NULL
);