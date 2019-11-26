-- lists all the cities of California.
SELECT
	id, name
FROM
	cities
WHERE
	name NOT IN (SELECT
	     name
	FROM
		states
	WHERE
		name = 'California');
