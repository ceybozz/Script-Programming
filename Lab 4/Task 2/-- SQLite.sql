-- SQLite
DROP TABLE IF EXISTS weather;

CREATE TABLE IF NOT EXISTS weather (
    City VARCHAR(50) UNIQUE,
    Temperature VARCHAR(5) NOT NULL,
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);

INSERT INTO weather (City, Temperature) 
    VALUES ('Stockhom', '-1'),
    ('Miami', '25'),
    ('Japan', '15'),
    ('Los Angeles', '5');