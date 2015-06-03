import fresh_tomatoes
import media

#init movies as a list
movies = []

#add movies to list
movies.append(media.Movie("Stardust",
              "http://ia.media-imdb.com/images/M/MV5BMjkyMTE1OTYwNF5BMl5BanBnXkFtZTcwMDIxODYzMw@@._V1_SX214_AL_.jpg",
              "https://www.youtube.com/watch?v=VfYBKDyF-Dk",
			  "2007",
			  '''In a countryside town bordering on a magical land, 
			  a young man makes a promise to his beloved that he'll retrieve a fallen star 
			  by venturing into the magical realm.''')
		)
movies.append(media.Movie("Boondock Saints",
              "http://ia.media-imdb.com/images/M/MV5BMTIzODA2NTUyM15BMl5BanBnXkFtZTYwODQ2Mjk4._V1__SX1303_SY619_.jpg",
              "https://www.youtube.com/watch?v=ydXojYfCF3I",
			  "1999",
			  "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.")
		)
movies.append(media.Movie("Stardust",
              "http://ia.media-imdb.com/images/M/MV5BMjkyMTE1OTYwNF5BMl5BanBnXkFtZTcwMDIxODYzMw@@._V1_SX214_AL_.jpg",
              "https://www.youtube.com/watch?v=VfYBKDyF-Dk",
			  "2007",
			  '''In a countryside town bordering on a magical land, 
			  a young man makes a promise to his beloved that he'll retrieve a fallen star 
			  by venturing into the magical realm.''')
		)
movies.append(media.Movie("Boondock Saints",
              "http://ia.media-imdb.com/images/M/MV5BMTIzODA2NTUyM15BMl5BanBnXkFtZTYwODQ2Mjk4._V1__SX1303_SY619_.jpg",
              "https://www.youtube.com/watch?v=ydXojYfCF3I",
			  "1999",
			  "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.")
		)

#call the web page maker		
fresh_tomatoes.open_movies_page(movies)
