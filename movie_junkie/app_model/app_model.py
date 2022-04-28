"""
    The app model component is responsible for interacting with and storing 
    the app data. It is interacted with through the app controller component. It provides
    a layer for interacting with the data from the higher level app logic.

    Author: Acadia Farrell (afarre11)
"""
import imdb 

class AppModel:
    def __init__(self):
        self.want_to_watch = {}
        self.have_watched = {}
        self.movie_notes = {}
        self.movie_repo = imdb.Cinemagoer()
        self.load_data()
        
    def load_data(self):
        """Loads want to watch list, have watched list, and movie notes
           from data files."""
        pass

    def save_data(self):
        """Saves want to watch list, have watched list, and movie notes
           to data files."""
        pass
        
    def add_movie_want_watch(self, movie_name):
        """Adds movie to the want to watch list, unless movie already exists."""
        pass

    def remove_movie_want_watch(self, movie_name):
        """Removes movie from want to watch list if movie is in list."""
        pass

    def get_want_watch(self):
        """Returns list of want to watch movies."""
        pass

    def add_movie_have_watched(self, movie_name):
        """Adds movie to the have watched list, unless movie already exists."""
        pass

    def remove_movie_have_watched(self, movie_name):
        """Removes movie from have watched list if movie is in list."""
        pass

    def get_have_watched(self):
        """Returns list of have watched movies."""
        pass

    def add_edit_movie_notes(self, movie_name):
        """Add new note for a specified movie. Replace exisiting note if it is already in 
           the notes list."""
        pass

    def remove_movie_note(self, movie_name):
        """Remove exising note for a specified movie, if it exists."""
        pass

    def get_movie_notes(self):
        """Returns list of movie notes."""
        pass

    def get_movie_reviews(self, movie_name):
        """Gets and returns list of movie reviews for a specified movie."""
        pass

    def get_movie_recs(self, keyword):
        """Gets and returns list of movie recommendations for a specified keyword"""
        pass