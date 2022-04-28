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

    def set_current(self, menu_code):
        """Sets the current menu state to the new, desired menu state. """
        self.current_menu = menu_code
    
    def display_title(self):
        """Displays the name of the program, Movie Junkie"""
        print('*' * 12)
        print('Movie Junkie')
        print('*' * 12)

    def display_main(self):
        """Acadia Farrell (afarre11) Presents the user with a menu of options.
        Prompts user for input. The input is validated and then returned
        to the main function as an integer"""
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

    def display_want_watch(self, formatted_movie_list):
        pass

    def display_have_watch(self, formatted_movie_list):
        pass

    def display_movie_notes(self, formatted_movie_notes):
        pass

    def display_movie_reviews(self, formatted_movie_reviews):
        pass

    def display_movie_reccomendations(self, formatted_movie_recs):
        pass
    
    def pretty_print_want_watch(self):
        pass

    def pretty_print_have_watched(self):
        pass

    def pretty_print_movie_notes(self):
        pass
        

