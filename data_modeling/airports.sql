CREATE TABLE IF NOT EXISTS airports (
    AirportCode                 VARCHAR(3) NOT NULL PRIMARY KEY,
    PositionCoordinateLatitude  NUMERIC(8,4) NOT NULL,
    PositionCoordinateLongitude NUMERIC(8,4) NOT NULL,
    AirportName                 VARCHAR(20) NOT NULL,
    CityCode                    VARCHAR(3) NOT NULL,
    CountryCode                 VARCHAR(2) NOT NULL,
    LocationType                VARCHAR(7) NOT NULL
);