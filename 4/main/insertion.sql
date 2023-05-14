-- musician
INSERT INTO musician ("name") VALUES('5''nizza');
INSERT INTO musician ("name") VALUES('Eminem');
INSERT INTO musician ("name") VALUES('Эпидемия');
INSERT INTO musician ("name") VALUES('Bob Marley');
INSERT INTO musician ("name") VALUES('The Prodigy');

-- genre
INSERT INTO genre (title) VALUES('Hip-hop');
INSERT INTO genre (title) VALUES('Raggae');
INSERT INTO genre (title) VALUES('Funk');
INSERT INTO genre (title) VALUES('Rap');
INSERT INTO genre (title) VALUES('Metall');
INSERT INTO genre (title) VALUES('Electropunk');
INSERT INTO genre (title) VALUES('Electronic Rock');

-- musician_genre
INSERT INTO musician_genre (musician_id, genre_id) VALUES(1, 1);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(1, 2);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(1, 3);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(2, 4);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(3, 5);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(4, 2);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(5, 6);
INSERT INTO musician_genre (musician_id, genre_id) VALUES(5, 7);

-- album
INSERT INTO album (title, release_date) VALUES('Пятница', 2003);
INSERT INTO album (title, release_date) VALUES('The Eminem Show', 2002);
INSERT INTO album (title, release_date) VALUES('Эльфийская Рукопись', 2004);
INSERT INTO album (title, release_date) VALUES('At the Apollo ''79', 2020);
INSERT INTO album (title, release_date) VALUES('Invaders Must Die', 2019);
INSERT INTO album (title, release_date) VALUES('КУ', 2020);

-- musician_album
INSERT INTO musician_album (musician_id, album_id) VALUES(1, 1);
INSERT INTO musician_album (musician_id, album_id) VALUES(2, 2);
INSERT INTO musician_album (musician_id, album_id) VALUES(3, 3);
INSERT INTO musician_album (musician_id, album_id) VALUES(4, 4);
INSERT INTO musician_album (musician_id, album_id) VALUES(5, 5);
INSERT INTO musician_album (musician_id, album_id) VALUES(1, 6);

-- track
INSERT INTO track (title, length, album_id) VALUES('Сюрная', 244, 1);
INSERT INTO track (title, length, album_id) VALUES('Пятница', 176, 1);
INSERT INTO track (title, length, album_id) VALUES('Curtains Up', 29, 2);
INSERT INTO track (title, length, album_id) VALUES('White America', 324, 2);
INSERT INTO track (title, length, album_id) VALUES('Час испытания', 296, 3);
INSERT INTO track (title, length, album_id) VALUES('Рожденный для битвы', 371, 3);
INSERT INTO track (title, length, album_id) VALUES('Natural music', 255, 4);
INSERT INTO track (title, length, album_id) VALUES('I shot the sheriff', 334, 4);
INSERT INTO track (title, length, album_id) VALUES('Omen', 216, 5);
INSERT INTO track (title, length, album_id) VALUES('Invaders must die', 295, 5);
INSERT INTO track (title, length, album_id) VALUES('my favourite track', 200, 2);
INSERT INTO track (title, length, album_id) VALUES('me myself and i', 245, 2);
INSERT INTO track (title, length, album_id) VALUES('Мой любимый трек', 333, 2);
INSERT INTO track (title, length, album_id) VALUES('A song of my', 222, 2);

-- digest
INSERT INTO digest (title, release_date) VALUES('Bob marley hits', 2018);
INSERT INTO digest (title, release_date) VALUES('Eminem hits', 2020);
INSERT INTO digest (title, release_date) VALUES('The Prodigy hits', 2022);
INSERT INTO digest (title, release_date) VALUES('Epidemy and 5''nizza best hits', 2019);

-- track_digest
INSERT INTO track_digest (track_id, digest_id) VALUES(7, 1);
INSERT INTO track_digest (track_id, digest_id) VALUES(8, 1);
INSERT INTO track_digest (track_id, digest_id) VALUES(3, 2);
INSERT INTO track_digest (track_id, digest_id) VALUES(4, 2);
INSERT INTO track_digest (track_id, digest_id) VALUES(9, 3);
INSERT INTO track_digest (track_id, digest_id) VALUES(10, 3);
INSERT INTO track_digest (track_id, digest_id) VALUES(1, 4);
INSERT INTO track_digest (track_id, digest_id) VALUES(2, 4);
INSERT INTO track_digest (track_id, digest_id) VALUES(5, 4);
INSERT INTO track_digest (track_id, digest_id) VALUES(6, 4);