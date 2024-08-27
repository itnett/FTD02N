-- Eksempel på avansert indeksering: Partiell indeks
CREATE INDEX idx_partial_alder ON elever (alder) WHERE alder > 18;

-- Geospatial indeks i PostgreSQL
CREATE EXTENSION postgis;
CREATE INDEX idx_geography ON steder USING GIST(geography);