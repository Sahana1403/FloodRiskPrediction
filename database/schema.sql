CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE basins (
    basin_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    geom GEOMETRY(POLYGON, 4326)
);

CREATE TABLE stations (
    station_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    geom GEOMETRY(POINT, 4326),
    latest_level FLOAT,
    last_update TIMESTAMP
);

CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    message TEXT,
    recipients TEXT[],
    sent_at TIMESTAMP DEFAULT NOW()
);
