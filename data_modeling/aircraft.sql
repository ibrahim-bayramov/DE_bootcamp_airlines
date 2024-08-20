CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_code      VARCHAR(3) NOT NULL PRIMARY KEY,
    language_code      VARCHAR(2),
    aircraft_name      VARCHAR(29),
    airline_equip_code VARCHAR(4) NOT NULL
);