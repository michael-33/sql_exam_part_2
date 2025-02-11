import sqlite3


def create_store_db():
	"""
	create db and insert data
	:return: conn, cursor
	"""
	try:
		# create db
		conn = sqlite3.connect('movies.db')
		cursor = conn.cursor()

		# create table
		cursor.execute('''
		CREATE TABLE IF NOT EXISTS movies (
		    id INTEGER PRIMARY KEY AUTOINCREMENT,
		    movie_name TEXT NOT NULL UNIQUE,
		    genre TEXT NOT NULL,
		    country TEXT NOT NULL,
		    language TEXT NOT NULL,
		    year INTEGER NOT NULL CHECK (year >= 2009),
		    revenue REAL NOT NULL CHECK (revenue >= 0)
		);
		''')

		movies_data = [
			('Oppenheimer', 'Biography', 'USA', 'English', 2023, 960),
			('Barbie', 'Comedy', 'USA', 'English', 2023, 1440),
			('Dune Part Two', 'Sci-Fi', 'USA', 'English', 2024, 700),
			('John Wick 4', 'Action', 'USA', 'English', 2023, 440),
			('Everything Everywhere All at Once', 'Sci-Fi', 'USA', 'English', 2022, 140),
			('The Batman', 'Action', 'USA', 'English', 2022, 772),
			('Spider Man No Way Home', 'Action', 'USA', 'English', 2021, 1920),
			('Top Gun Maverick', 'Action', 'USA', 'English', 2022, 1490),
			('The Whale', 'Drama', 'USA', 'English', 2022, 55),
			('Guardians of the Galaxy Vol 3', 'Action', 'USA', 'English', 2023, 845),
			('Parasite', 'Thriller', 'South Korea', 'Korean', 2019, 266),
			('Train to Busan 2', 'Horror', 'South Korea', 'Korean', 2020, 92),
			('Decision to Leave', 'Mystery', 'South Korea', 'Korean', 2022, 23),
			('Joker', 'Drama', 'USA', 'English', 2019, 1074),
			('Tenet', 'Sci-Fi', 'USA', 'English', 2020, 365),
			('The Irishman', 'Crime', 'USA', 'English', 2019, 8),
			('Ford v Ferrari', 'Drama', 'USA', 'English', 2019, 225),
			('1917', 'War', 'UK', 'English', 2019, 385),
			('The Farewell', 'Drama', 'USA', 'English/Chinese', 2019, 23),
			('The Banshees of Inisherin', 'Comedy', 'Ireland', 'English', 2022, 49),
			('Django Unchained', 'Western', 'USA', 'English', 2012, 426),
			('Avengers Endgame', 'Action', 'USA', 'English', 2019, 2798),
			('Black Panther', 'Action', 'USA', 'English', 2018, 1347),
			('Coco', 'Animation', 'USA', 'English/Spanish', 2017, 807),
			('Mad Max Fury Road', 'Action', 'Australia', 'English', 2015, 380),
			('Inception', 'Sci-Fi', 'USA', 'English', 2010, 837),
			('The Revenant', 'Adventure', 'USA', 'English', 2015, 532),
			('La La Land', 'Musical', 'USA', 'English', 2016, 447),
			('The Secret in Their Eyes', 'Crime', 'Argentina', 'Spanish', 2009, 34),
			('No Time to Die', 'Action', 'UK', 'English', 2021, 774)]

		# insert data
		cursor.executemany('''
		INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES (?, ?, ?, ?, ?, ?)
		''', movies_data)

		conn.commit()

		return conn, cursor
	except sqlite3.Error as e:
		print(f'Error: {e}')


# section a
def show_all_movies(cursor):
	"""
	print all movies
	:param cursor:
	"""
	cursor.execute('''
		SELECT * FROM movies
		''')

	results = cursor.fetchall()
	for movie in results:
		print(movie)


# section b
def search_movie(cursor):
	"""
	search movie by name or partial name
	:param cursor:
	"""
	name = input('Enter movie name or part of it: ')
	cursor.execute('''
		SELECT movie_name FROM movies
		WHERE movie_name LIKE ?
		''', (f'%{name}%',))

	results = cursor.fetchall()
	for movie in results:
		print(movie)


# section c
def add_movie(conn, cursor):
	"""
	add movie to db
	:param conn:
	:param cursor:
	"""
	# get movie data
	movie_name = input('Enter movie name')
	genre = input('Enter movie genre')
	country = input('Enter movie country')
	language = input('Enter movie language')
	year = input('Enter movie year')
	revenue = input('Enter movie revenue')
	movie_data = (movie_name, genre, country, language, year, revenue)

	try:
		# insert movie data
		cursor.execute('''
		INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES (?, ?, ?, ?, ?, ?)
		''', movie_data)
		# save changes
		conn.commit()
		print("movie was successfully added")
	except sqlite3.Error as e:
		print(f'Error: {e}')
		conn.rollback()


def run_project():
	conn = None
	try:
		connection, cursor = create_store_db()
		conn = connection
		search_movie(cursor)
		add_movie(conn, cursor)
		show_all_movies(cursor)
	except Exception as e:
		print(f'Error: {e}')
	finally:
		if conn:
			conn.close()


run_project()
