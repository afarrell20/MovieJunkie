"""
    The app model component is responsible for interacting with and storing 
    the app data. It is interacted with through the app controller component. It provides
    a layer for interacting with the data from the higher level app logic.

    Author: Maggie Whittier (mewhitti)
"""
class AppModel:
    def __init__(self):
        self.want_to_watch = {}
        self.have_watched = {}
        self.movie_notes = {}
        self.movie_repo = None
        self.load_want_watch()
        self.load_have_watched()
        self.load_movie_notes()
        
    def load_want_watch(self):
        pass

    def load_have_watched(self):
        pass

    def load_movie_notes(self):
        pass

    def pretty_print_want_watch(self):
        pass

    def pretty_print_have_watched(self):
        pass

    def pretty_print_movie_notes(self):
        pass
        