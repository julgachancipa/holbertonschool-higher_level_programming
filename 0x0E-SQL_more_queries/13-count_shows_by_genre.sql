-- lists all shows contained in hbtn_0d_tvshows
SELECT
	tv_genres.name, COUNT(tv_show_genres.genre_id) as genre
FROM
	tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY genre DESC
;
