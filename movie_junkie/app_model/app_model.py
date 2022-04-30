"""
    The app model component is responsible for interacting with and storing 
    the app data. It is interacted with through the app controller component. It provides
    a layer for interacting with the data from the higher level app logic.

    Author: Acadia Farrell (afarre11)
"""
import imdb 
import pickle 


FOLDER_PATH = "movie_junkie/app_model/data/"
WANT_WATCH_PATH = FOLDER_PATH + "want_watch_list_data.pickle"
HAVE_WATCHED_PATH = FOLDER_PATH + "have_watched_list_data.pickle"
MOVIE_NOTES_PATH = FOLDER_PATH + "movie_notes_list_data.pickle"


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
        try:
            with open(WANT_WATCH_PATH, "rb") as want_watch_file:
                self.want_to_watch = pickle.load(want_watch_file) 
        except FileNotFoundError:
            self.want_to_watch = {}
        
        # Have watched list 
        try:
            with open(HAVE_WATCHED_PATH, "rb") as have_watched_file:
                self.have_watched = pickle.load(have_watched_file) 
        except FileNotFoundError:
            self.have_watched = {}
        
        # Movie notes list
        try:
            with open(MOVIE_NOTES_PATH, "rb") as movie_notes_file:
                self.movie_notes = pickle.load(movie_notes_file) 
        except FileNotFoundError:
            self.movie_notes = {}

    def save_data(self):
        """Saves want to watch list, have watched list, and movie notes
           to data files."""
        # Want to watch movie list
        try:
            with open(WANT_WATCH_PATH, "wb") as want_watch_file:
                pickle.dump(self.want_to_watch, want_watch_file, pickle.HIGHEST_PROTOCOL) 
        except FileNotFoundError:
            self.want_to_watch = {}
        
        # Have watched list 
        try:
            with open(HAVE_WATCHED_PATH, "wb") as have_watched_file:
               pickle.dump(self.have_watched, have_watched_file, pickle.HIGHEST_PROTOCOL)  
        except FileNotFoundError:
            self.have_watched = {}
        
        # Movie notes list
        try:
            with open(MOVIE_NOTES_PATH, "wb") as movie_notes_file:
                pickle.dump(self.movie_notes, movie_notes_file, pickle.HIGHEST_PROTOCOL) 
        except FileNotFoundError:
            self.movie_notes = {}
      
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
        try:
            # Get movie review data
            search = self.movie_repo.search_movie(movie_name)
            movie = search[0]
            self.movie_repo.update(movie, info = ['reviews'])
            review_data = movie.get('reviews')

            # Clean up movie review data
            reviews = []
            for i in range(len(review_data)):
                if i < 5:
                    reviews.append(review_data[i]['content'])
            
            return reviews
        except imdb.IMDbError:
            return "*** Reviews could not be retrieved ***"

    def get_movie_recommendations(self, keyword):
        """Gets and returns list of movie recommendations for a specified keyword"""
        try:
            recs_list = self.movie_repo.get_keyword(keyword)
            return recs_list[0:5]
        except imdb.IMDbError:
            return "*** Recommendations could not be retrieved ***"