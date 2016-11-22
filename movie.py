import webbrowser
class Movies():
    """ This class stores movie related information """
    # Initialize the class Movies object
    def __init__(self, movie_title_new, movie_summary_new, movie_image_new, movie_trailer_new):
        self.title =  movie_title_new
        self.storyline = movie_summary_new
        self.poster_image_url = movie_image_new
        self.trailer_youtube_url = movie_trailer_new
    # Function which shows the movie youtube trailer when clicked on movie tile.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
