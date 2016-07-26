# Media

# This code defines the Movie class


class Movie():

    # Default documentation

    """This class stores movie-related information"""

    # Constructor requires all movie information to be provided

    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube):

        """The default Movie constructor requires movie_title,
        movie_storyline, poster_image (a url link to the poster
        image), and trailer_youtube (a url link to the YouTube
        movie trailer)."""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
