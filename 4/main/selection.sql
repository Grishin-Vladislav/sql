-- longest track
select title as "track name", length as "length (sec)"
from track
where length = (select max(length) from track);

-- tracks longer than 3.5 minutes (210 seconds)
select title as "track name", length as "length (sec)"
from track
where length > 210;

-- digests from 2018 to 2020 inclusive
select title as digest, "release date" 
from digest
where release_date between 2018 and 2020;

-- musician name having one word
select name as "artist name"
from musician
where array_length(string_to_array("name", ' '), 1) = 1;

-- tracks with 'my' or 'мой' words
select title as track
from track
where (string_to_array(lower(title), ' ')) && array ['my','мой'];

-- how many musicians in each genre
select g.title as genre, count(m.name) as "total artists"
from musician m
join musician_genre mg on m.musician_id = mg.musician_id
join genre g on mg.genre_id = g.genre_id
group by g.title;

-- how many tracks in albums from 2019-2020
select count(t.title) as "2019-2020 tracks"
from track t
join album a ON t.album_id  = a.album_id
where a.release_date between 2019 and 2020;

-- average track length by albums
select a.title as album, avg(t.length) as "average length (sec)"
from track t
join album a on t.album_id = a.album_id
group by a.title;

-- musicians that did not released albums in 2020
select distinct m.name
from musician m
where not exists (
  select 1
  from musician_album ma
  join album a on ma.album_id = a.album_id
  where ma.musician_id = m.musician_id
    and a.release_date = 2020
);

-- digests with selected musician
select d.title
from digest d
join track_digest td on d.digest_id = td.digest_id
join track t on td.track_id = t.track_id 
join album a on t.album_id = a.album_id 
join musician_album ma on a.album_id = ma.album_id
join musician m on ma.musician_id = m.musician_id
where name = '5''nizza'
group by d.title;




