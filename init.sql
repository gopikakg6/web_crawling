DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(50));



CREATE TABLE songs(
    id SERIAL PRIMARY KEY ,
    song_name VARCHAR(80),
    artist_id INTEGER REFERENCES artists(id),
    lyrics text
    
);