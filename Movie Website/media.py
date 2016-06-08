import webbrowser
class Movie():
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, movie_rating, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        