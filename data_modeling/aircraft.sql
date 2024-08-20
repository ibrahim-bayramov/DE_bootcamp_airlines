CREATE TABLE IF NOT EXISTS aircraft (
    AircraftCode      VARCHAR(3) NOT NULL PRIMARY KEY,
    LanguageCode      VARCHAR(2) NOT NULL,
    Aircraft_Name     VARCHAR(29) NOT NULL,
    AirlineEquipCode  VARCHAR(4) NOT NULL
);