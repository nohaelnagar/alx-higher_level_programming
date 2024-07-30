-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT shows.title, genres.genre_id
  FROM tv_shows AS shows
       LEFT JOIN tv_show_genres AS genres
       ON shows.id = genres.show_id
       WHERE genres.genre_id IS NULL
 ORDER BY shows.title, genres.genre_id;
