CREATE TABLE IF NOT EXISTS countries (
    country_code VARCHAR(2) PRIMARY KEY,
    names JSONB,
    meta JSONB
);
