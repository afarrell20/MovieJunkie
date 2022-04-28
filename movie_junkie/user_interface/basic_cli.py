"""
    Basic command line interface component for the app. The user interface 
    component is responsible for displaying the menus and getting input from the user.
    The user interface component is controlled by the app controller component to display 
    the correct content. The user interface component can receive formatted text to display 
    from the app controller component if applicable. 
    
    Author: Maggie Whittier (mewhitti)
"""
import movie_junkie.user_interface.interface_codes as codes


class UserInterface:
    def __init__(self):
        self.current_menu = codes.MAIN
    
    def user_input(self, prompt):
        """Get input from user and process input to return either an action code
           (menu choice) or desired input (i.e. movie name, keyword, etc.)."""
        pass
    
    def display_title(self):
        """Displays the name of the program, Movie Junkie."""
        print('*' * 12)
        print('Movie Junkie')
        print('*' * 12)

    def display_error(self, error_message):
        """Utility function for displaying error messages to the interface to prevent code
           from crashing."""
        pass

    def display_message(self, message):
        """Utility function for displaying general messages to the interface."""
        pass

    def display_main(self):
        """Displays main menu.
           
        Author: Acadia Farrell (afarre11)
        """
        self.current_menu = codes.MAIN

        print('\nSelect from the options below: ')
        one = '1. Want to Watch List'
        two = '2. Have Watched List'
        three = '3. My Movie Notes'
        four = '4. View Critic Ratings'
        five = '5. Get Movie Recommendation'
        six = '6. Quit'
        print(f'\n{one:>26}')
        print(f'{two:>25}')
        print(f'{three:>22}')
        print(f'{four:>27}')
        print(f'{five:>32}')
        print(f'{six:>12}')

    def display_want_watch(self, movie_list):
        """Displays want to watch menu."""
        pass

    def display_have_watch(self, movie_list):
        """Displays have watched menu."""
        pass

    def display_movie_notes(self, movie_notes):
        """Displays movie notes menu."""
        pass

    def display_movie_reviews(self, movie_reviews):
        """Displays movie review menu."""
        pass

    def display_movie_recommendations(self, movie_recs):
        """Displays movie recommendation menu."""
        pass
    
    def pretty_print_movie_list(self, movie_list):
        """Displays specified movie list in an organized manner. If multiple movies are in 
           the list, only the first four movies and the final movie at the end
           are displayed with ... in the middle. Prints each movie on a seperate line
           in alphabetical order. 
           Example:

            Dumb and Dumber
            Dune
            Lovie, Rosie
            Pitch Perfect 2   
            ...
            Ten Things I Hate About You
        """
        pass

    def pretty_print_movie_notes(self, movie_notes):
        """Displays specified movie list with notes in an organized manner. If multiple movies are in 
           the list, only the first four movies and the final movie at the end
           are displayed with ... in the middle. Prints each movie on a seperate line
           in alphabetical order. 
           Example:

            Dumb and Dumber --> Note
            Dune --> Note
            Lovie, Rosie --> Note
            Pitch Perfect 2 --> Note 
            ...
            Ten Things I Hate About You --> Note
        """
        pass