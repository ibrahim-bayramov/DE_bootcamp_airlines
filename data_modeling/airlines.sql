CREATE TABLE IF NOT EXISTS airlines (
    AirlineID             VARCHAR(2) NOT NULL PRIMARY KEY,
    AirlineID_ICAO        VARCHAR(3),
    Airlines_LanguageCode VARCHAR(2) NOT NULL,
    Airlines_Name         VARCHAR(41) NOT NULL
);