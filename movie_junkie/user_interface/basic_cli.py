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
        user_input = input(prompt)

        try:
            action_code = int(str(self.current_menu) + user_input)
            return action_code
        except ValueError:
            return user_input
    
    def display_title(self):
        """Displays the name of the program, Movie Junkie."""
        print('*' * 12)
        print('Movie Junkie')
        print('*' * 12)

    def display_error(self, error_message):
        """Utility function for displaying error messages to the interface to prevent code
           from crashing."""
        print()
        print(error_message)

    def display_message(self, message):
        """Utility function for displaying general messages to the interface."""
        print()
        print(message)

    def display_main(self):
        """Displays main menu.
           
        Author: Acadia Farrell (afarre11)
        """
        self.current_menu = codes.MAIN

        print('\nSelect from the options below: ')
        one = '1. Want to Watch List'
        two = '2. Have Watched List'
        three = '3. My Movie Notes'
        four = '4. Get movie reviews'
        five = '5. Get Movie Recommendations'
        six = '6. Quit'
        print(f'\n{one:>26}')
        print(f'{two:>25}')
        print(f'{three:>22}')
        print(f'{four:>25}')
        print(f'{five:>33}')
        print(f'{six:>12}')

    def display_want_watch(self, movie_list):
        """Displays want to watch menu."""
        self.current_menu = codes.WANT

        print("\n--- Want To Watch Movie List ---")
        print()
        self.pretty_print_movie_list(movie_list)
        print('\nSelect from the options below: ')
        one = '1. Add Movie'
        two = '2. Remove Movie'
        third = '3. Exit to Main Menu'
        print(f'\n{one:>17}')
        print(f'{two:>20}')
        print(f'{third:>25}')

    def display_have_watch(self, movie_list):
        """Displays have watched menu."""
        self.current_menu = codes.HAVE

        print("\n--- Have Watched Movie List ---")
        print()
        self.pretty_print_movie_list(movie_list)
        print('\nSelect from the options below: ')
        one = '1. Add Movie'
        two = '2. Remove Movie'
        three = '3. Exit to Main Menu'
        print(f'\n{one:>17}')
        print(f'{two:>20}')
        print(f'{three:>25}')

    def display_movie_notes(self, movie_notes):
        """Displays movie notes menu."""
        self.current_menu = codes.NOTES

        self.pretty_print_movie_notes(movie_notes)
        print('\nSelect from the options below: ')
        one = '1. Add/Edit Movie Note'
        two = '2. Remove Movie Note'
        three = '3. Exit to Main Menu'
        print(f'\n{one:>27}')
        print(f'{two:>25}')
        print(f'{three:>25}')

    def display_movie_reviews(self, movie_reviews):
        """Displays movie review menu."""
        self.current_menu = codes.REVIEWS
    
        self.pretty_print_movie_reviews(movie_reviews)
        self.display_main()
    
    def display_movie_recommendations(self, movie_recs):
        """Displays movie recommendation menu."""
        self.current_menu = codes.RECOMMENDATIONS

        print("\n--- Recommendations ---")
        print()
        self.pretty_print_movie_list(movie_recs)
        self.display_main()

    def pretty_print_movie_list(self, movie_list):
        """Displays specified movie list in an organized manner. Prints each movie on a seperate line
           in alphabetical order. 
           Example:

            Dumb and Dumber
            Dune
            Lovie, Rosie
            Pitch Perfect 2   
            ...
            Ten Things I Hate About You
        """
        if type(movie_list) == dict or type(movie_list) == list:
            for movie in sorted(movie_list):
                print(movie)
        else:
            print(movie_list)

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
        print()
        print("--- Movie Notes ---")
        print()
        if type(movie_notes) == dict:
            for movie in sorted(movie_notes):
                print(f'{movie} --> {movie_notes[movie]}')
        else:
            print(movie_notes)

    def pretty_print_movie_reviews(self, movie_reviews):
        """Displays specified movie reviews in an organized manner. Prints each review on a seperate 
           line, separated by a line. """
        try:
            print()
            print("--- Reviews ---")
            for review in movie_reviews:
                print(f"\n{review['content']}")
                print()
                print()
        except TypeError:
            self.display_error(movie_reviews)