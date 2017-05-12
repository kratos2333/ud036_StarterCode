import webbrowser

class Movie() :
    ''' The class provides a way to store movie related information '''
    VALID_RATING = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
    	# this constructor will initial the following instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
