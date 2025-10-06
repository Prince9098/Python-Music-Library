-- Schema for Music Library
CREATE TABLE IF NOT EXISTS artists (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS albums (
  id INT AUTO_INCREMENT PRIMARY KEY,
  artist_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  year SMALLINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tracks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  album_id INT,
  title VARCHAR(255) NOT NULL,
  length_seconds INT DEFAULT 0,
  genre VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS playlists (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playlist_tracks (
  playlist_id INT NOT NULL,
  track_id INT NOT NULL,
  position INT DEFAULT 0,
  PRIMARY KEY (playlist_id, track_id),
  FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
  FOREIGN KEY (track_id) REFERENCES tracks(id) ON DELETE CASCADE
);

-- sample data
INSERT INTO artists (name) VALUES ('Radiohead'), ('Daft Punk'), ('A.R. Rahman');
INSERT INTO albums (artist_id, title, year) VALUES (1,'OK Computer',1997), (2,'Discovery',2001), (3,'Slumdog Millionaire OST',2008);
INSERT INTO tracks (album_id, title, length_seconds, genre) VALUES (1,'Paranoid Android',387,'Alternative'), (1,'Karma Police',260,'Alternative'), (2,'One More Time',321,'Electronic'), (3,'Jai Ho',254,'Soundtrack');
INSERT INTO playlists (name) VALUES ('Road Trip'), ('Coding Mix');
INSERT INTO playlist_tracks (playlist_id, track_id, position) VALUES (1,1,1), (1,3,2), (2,2,1);
