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
movies.append(media.Movie("Spaceballs",
              "http://ia.media-imdb.com/images/M/MV5BMTM3Mzg0Mzc2NF5BMl5BanBnXkFtZTcwNDEwNTk0NA@@._V1_SX214_AL_.jpg",
              "https://www.youtube.com/watch?v=0uzEgsHypgM",
			  "1987",
			  "Planet Spaceball's President Skroob sends Lord Dark Helmet to steal Planet Druidia's abundant supply of air to replenish their own, and only Lone Starr can stop them.")
		)
movies.append(media.Movie("Dead Snow 2: Red vs. Dead",
              "http://ia.media-imdb.com/images/M/MV5BMTk2MTEwOTcwOF5BMl5BanBnXkFtZTgwMDEzMjM2MjE@._V1__SX1303_SY619_.jpg",
              "https://www.youtube.com/watch?v=n4FoV9iiLmI",
			  "2014",
			  "Still on the run from a group of Nazi zombies, a man seeks the aid of a group of American zombie enthusiasts, and discovers new techniques for fighting the zombies.")
		)

#call the web page maker		
fresh_tomatoes.open_movies_page(movies)
