class Movie:
	#constructor requiring moviews to have title, poster image url and youtube trailer url
	def __init__(self, title, poster_image_url, trailer_youtube_url, release_date, tag_line):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.release_date = release_date
		self.tag_line = tag_line