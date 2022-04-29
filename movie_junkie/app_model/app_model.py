"""
    The app model component is responsible for interacting with and storing 
    the app data. It is interacted with through the app controller component. It provides
    a layer for interacting with the data from the higher level app logic.

    Author: Acadia Farrell (afarre11)
"""
import imdb 
import pickle 

FOLDER_PATH = "movie_junkie/app_model/data/"


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

        # Want to watch movie list
        want_watch_file_path = FOLDER_PATH + "want_watch_list_data.pickle"
        with open(want_watch_file_path, "rb") as want_watch_file:
            self.want_to_watch = pickle.load(want_watch_file) 

    def save_data(self):
        """Saves want to watch list, have watched list, and movie notes
           to data files."""

        # Want to watch movie list
        want_watch_file_path = FOLDER_PATH + "want_watch_list_data.pickle"
        with open(want_watch_file_path, "wb") as want_watch_file:
            pickle.dump(self.want_to_watch, want_watch_file, pickle.HIGHEST_PROTOCOL)

        
    def add_movie_want_watch(self, movie_name):
        """Adds movie to the want to watch list, unless movie already exists. Returns result."""
        if movie_name not in self.want_to_watch:
            self.want_to_watch[movie_name] = 'NO_VALUE_NEEDED'
            return (f'*** {movie_name} has been added to the want to watch list ***')
        else:
            return (f'*** {movie_name} is already in the want to watch list ***')

    def remove_movie_want_watch(self, movie_name):
        """Removes movie from want to watch list if movie is in list. Returns result."""
        try:
            self.want_to_watch.pop(movie_name)
            return (f'*** {movie_name} has been removed from the want to watch list ***')
        except KeyError:
            return (f'*** {movie_name} is not in the want to watch list ***')

    def get_want_watch(self):
        """Returns list of want to watch movies."""
        return list(self.want_to_watch.keys())

    def add_movie_have_watched(self, movie_name):
        """Adds movie to the have watched list, unless movie already exists. Returns result."""
        if movie_name not in self.have_watched:
            self.have_watched[movie_name] = 'NO_VALUE_NEEDED'
            return (f'*** {movie_name} has been added to the have watched list ***')
        else:
            return (f'*** {movie_name} is already in the have watched list ***')

    def remove_movie_have_watched(self, movie_name):
        """Removes movie from have watched list if movie is in list. Returns result."""
        try:
            self.have_watched.pop(movie_name)
            return (f'*** {movie_name} has been removed from the have watched list ***')
        except KeyError:
            return (f'*** {movie_name} is not in the have watched list ***')

    def get_have_watched(self):
        """Returns list of have watched movies."""
        return list(self.have_watched.keys())

    def add_edit_movie_notes(self, movie_name, movie_note):
        """Add new note for a specified movie. Replace exisiting note if it is already in 
           the notes list. Returns result."""
        if movie_name not in self.movie_notes:
            self.movie_notes[movie_name] = movie_note
            return (f'*** Note for {movie_name} has been added to the movie notes list ***')
        else:
            self.movie_notes[movie_name] = movie_note
            return (f'*** Note for {movie_name} updated in the movie notes list ***')

    def remove_movie_note(self, movie_name):
        """Remove exising note for a specified movie, if it exists. Returns result."""
        try:
            self.movie_notes.pop(movie_name)
            return (f'*** Note for {movie_name} has been removed from the movie notes list ***')
        except KeyError:
            return (f'*** Note for {movie_name} is not in the movie notes list ***')

    def get_movie_notes(self):
        """Returns list of movie notes."""
        return self.movie_notes

    def get_movie_reviews(self, movie_name):
        """Gets and returns list of movie reviews for a specified movie."""
        pass

    def get_movie_recs(self, keyword):
        """Gets and returns list of movie recommendations for a specified keyword"""
        pass