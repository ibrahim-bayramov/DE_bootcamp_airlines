CREATE TABLE IF NOT EXISTS cities (
    CityCode                VARCHAR(3) NOT NULL PRIMARY KEY,
    CountryCode             VARCHAR(2) NOT NULL,
    UtcOffset               VARCHAR(6) NOT NULL,
    TimeZoneId              VARCHAR(19),
    City_Name                VARCHAR(50) NOT NULL,
    AssociatedAirports      VARCHAR(3)[]
);
