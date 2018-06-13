import webbrowser


class Movie():
    """Stores movie related information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # Defines the instance variables to store movie information.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens a youtube trailer link in a browser.
        webbrowser.open(self.trailer_youtube_url)
