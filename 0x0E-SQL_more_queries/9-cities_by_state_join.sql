-- lists all cities contained in the database.
SELECT
	cities.id, cities.name, states.name
FROM
	cities
LEFT JOIN states USING(id)
ORDER BY cities.id ASC;
