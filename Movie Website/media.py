import webbrowser
class Movie():
    """
    this class defines the basic structure of Movie objects.
    """
    
    def __init__(self, movie_title, movie_storyline, movie_rating, poster_image, youtube_trailer):
        """
        this constructor method takes 5 strings as input 
        1 --> Movie Title
        2 --> Storyline
        3 --> IMDB rating
        4 --> Link to poster Image
        5 --> Link to youtube trailer
        this function does not return anything
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    
    def show_trailer(self):
        """
        This fuction does not take any input and opens youtube trailer of the movie instance for which this fuction is called.
        """
        webbrowser.open(self.trailer_youtube_url)
        