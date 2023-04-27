create database music;

create table genre (
	genre_id serial primary key,
	title varchar(60)
);

create table musician (
	musician_id serial primary key,
	name varchar(60)
);

create table musician_genre (
	musician_id integer references musician (musician_id),
	genre_id integer references genre (genre_id)
);

create table album (
	album_id serial primary key,
	title varchar(60),
	release_date date
);

create table musician_album (
	musician_id integer references musician (musician_id),
	album_id integer references album (album_id)
);

create table track (
	track_id serial primary key,
	title varchar(100),
	length time,
	album_id integer references album (album_id)
);

create table digest (
	digest_id serial primary key,
	title varchar(60),
	release_date date
);

create table track_digest (
	track_id integer references track (track_id),
	digest_id integer references digest (digest_id)
);

