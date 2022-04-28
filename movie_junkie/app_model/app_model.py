"""
    The app model component is responsible for interacting with and storing 
    the app data. It is interacted with through the app controller component. It provides
    a layer for interacting with the data from the higher level app logic.

    Author: Acadia Farrell (afarre11)
"""
import cinemagoer 

class AppModel:
    def __init__(self):
        self.want_to_watch = {}
        self.have_watched = {}
        self.movie_notes = {}
        self.movie_repo = Cinemagoer()
        self.load_data()
        
    def load_data(self):
        """Loads want to watch list, have watched list, and movie notes
           from data files."""
        pass

    def save_data(self):
        """Saves want to watch list, have watched list, and movie notes
           to data files."""
        pass
        
    def add_movie_to_list(self, movie_name, list_name):
        """Adds movie to specified list if movie is not already in
           list."""
        pass

    def remove_movie_to_list(self, movie_name, list_name):
        """Removes movie from specified list if movie is in list."""
        pass

    def add_edit_movie_notes(self, movie_name):
        """Add new note for a specified movie. Replace exisiting note if it is already in 
           the notes list."""
        pass

    def get_movie_reviews(self, movie_name):
        """Gets and returns list of movie reviews for a specified movie."""
        pass

    def get_movie_recs(self, keyword):
        """Gets and returns list of movie recommendations for a specified keyword"""
        pass