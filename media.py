import webbrowser


class Movie():
    """ This class is used for storing the info about movies.
    Attributes:
        movie_title:       Movie Title as a string
        movie_duration:    Duration of the movie as a string
        movie_description: Storyline of the movie as a string
        movie_genre:       Genre of the movie as a string
        movie_release:     Release date as a string
        movie_main_actors: Main actors inside the movie as a string
        poster_image:      Url of the video poster image as a string
        trailer_youtube:   Url of the youtube trailer as a string
    """
    def __init__(self, movie_title, movie_duration, movie_description,
                 movie_genre, movie_release, movie_main_actors, poster_image,
                 trailer_youtube):
        """Initialises the Movie class instance variables."""
        self.title = movie_title
        self.duration = movie_duration
        self.description = movie_description
        self.genre = movie_genre
        self.release = movie_release
        self.main_actors = movie_main_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open the web browser to show the youtube movie trailer """
        webbrowser.open(self.trailer_youtube_url)
