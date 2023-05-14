create database music;

create table genre (
	genre_id serial primary key,
	title varchar(60) not null unique
);

create table musician (
	musician_id serial primary key,
	name varchar(60) not null unique
);

create table musician_genre (
	musician_id integer references musician (musician_id) on delete cascade,
	genre_id integer references genre (genre_id) on delete cascade
);

create table album (
	album_id serial primary key,
	title varchar(60) not null unique,
	release_date integer not null
);

create table musician_album (
	musician_id integer references musician (musician_id) on delete cascade,
	album_id integer references album (album_id) on delete cascade
);

create table track (
	track_id serial primary key,
	title varchar(100),
	length integer,
	album_id integer references album (album_id) on delete cascade
);

create table digest (
	digest_id serial primary key,
	title varchar(60) not null unique,
	release_date integer not null
);

create table track_digest (
	track_id integer references track (track_id) on delete cascade,
	digest_id integer references digest (digest_id) on delete cascade
);
