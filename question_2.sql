-- section 1
SELECT
	genre,
	COUNT(*) as num_of_movies
FROM movies
GROUP BY genre;

-- section 2
SELECT
	year,
	SUM(revenue) as total_revenue
FROM movies
GROUP BY year;

-- section 3
SELECT
	genre,
	ROUND(AVG(revenue), 2) as avg_revenue
FROM movies
GROUP BY genre;

-- section 4
SELECT
	genre,
	language,
	ROUND(AVG(revenue), 2) as avg_revenue
FROM movies
GROUP BY genre, language;

-- section 5
SELECT language
FROM (
    SELECT
        language,
        COUNT(*) as num_of_movies
    FROM movies
    GROUP BY language
    ORDER BY num_of_movies ASC
    LIMIT 1
);

-- section 6
SELECT country
FROM (
    SELECT
        country,
        COUNT(*) as num_of_movies
    FROM movies
    GROUP BY country
    ORDER BY num_of_movies DESC
    LIMIT 1
);

-- section 7
SELECT genre
FROM (
    SELECT
        genre,
        COUNT(*) as num_of_movies
    FROM movies
    GROUP BY genre
    HAVING num_of_movies > 2
);

-- section 8
SELECT year
FROM (
    SELECT
        year,
        SUM(revenue) as total_revenue
    FROM movies
    GROUP BY year
    HAVING total_revenue > 1000
);

-- section 9
SELECT language
FROM (
    SELECT
        language,
        COUNT(*) as num_of_movies
    FROM movies
    GROUP BY language
    HAVING num_of_movies >= 3
);