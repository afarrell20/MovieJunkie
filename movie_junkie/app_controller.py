"""
    App controller component acts as core of application. It handles processing of user input from the 
    user interface and acts on the model if applicable. Also responsible for interacting with and
    updating user interface. 
    
    Author: Maggie Whittier (mewhiiti)
"""
import movie_junkie.user_interface.interface_codes as codes


class AppController:
    def __init__(self, app_model, user_interface):
        self.app_model = app_model
        self.user_interface = user_interface
        self.app_running = True
        self.user_interface.display_title()
        self.user_interface.display_main()

    def next_action(self):
        """Get user input from user interface and process the input to execute the 
           associated action.
           
           Authors: Acadia Farrell and Maggie Whittier   
        """
        action_code = self.user_interface.user_input("Select from the menu options: ")
        
        # User on Main Menu, selects to go to Want to Watch Menu
        if action_code == codes.MAIN_WANT:
            want_watch_list = self.app_model.get_want_watch()
            self.user_interface.display_want_watch(want_watch_list)
         # User on Main Menu, selects to go to Have to Watch Menu   
        elif action_code == codes.MAIN_HAVE:
            have_watched_list = self.app_model.get_have_watched()
            self.user_interface.display_have_watch(have_watched_list)
        # Calls main menu for movie notes
        elif action_code == codes.MAIN_NOTES:
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_movie_notes(movie_notes_list)
        # Calls main menu for reviews
        elif action_code == codes.MAIN_REVIEWS:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            reviews = self.app_model.get_movie_reviews(movie_name)
            self.user_interface.display_movie_reviews(reviews)
        # Calls main menu for recs
        elif action_code == codes.MAIN_RECOMMENDATIONS:
            keyword = self.user_interface.user_input("Enter a movie keyword(ex: slapstick-comedy): ")
            recommendations = self.app_model.get_movie_recommendations(keyword)
            self.user_interface.display_movie_recommendations(recommendations)
        # Main menu quit function. Displays thank you message
        elif action_code == codes.MAIN_QUIT:
            self.app_model.save_data()
            self.user_interface.display_message("*** Thank you for using MovieJunkie ***")
            self.quit_app()
        # Calls function to allow user to enter movie to watchlist
        elif action_code == codes.WANT_WATCH_ADD:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            result = self.app_model.add_movie_want_watch(movie_name)
            movie_list = self.app_model.get_want_watch()
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch(movie_list)
        # Calls function to allow user to remove movie from watchlist
        elif action_code == codes.WANT_WATCH_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove: ")
            result = self.app_model.remove_movie_want_watch(movie_name)
            movie_list = self.app_model.get_want_watch()
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch(movie_list)
        # Main menu for watchlist
        elif action_code == codes.WANT_WATCH_MAIN:
            self.user_interface.display_main()
        # Calls function to allow user to add movie to watched list
        elif action_code == codes.HAVE_WATCHED_ADD:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            result = self.app_model.add_movie_have_watched(movie_name)
            movie_list = self.app_model.get_have_watched()
            self.user_interface.display_message(result)
            self.user_interface.display_have_watch(movie_list) # error somewhere here
        # Calls function to allow user to remove from have watched list 
        elif action_code == codes.HAVE_WATCHED_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove: ")
            result = self.app_model.remove_movie_have_watched(movie_name)
            movie_list = self.app_model.get_have_watched()
            self.user_interface.display_message(result)
            self.user_interface.display_have_watch(movie_list)
        # Calls main menu for have watched 
        elif action_code == codes.HAVE_WATCHED_MAIN:
            self.user_interface.display_main()
        # Calls function to add to notes list
        elif action_code == codes.NOTES_ADD:
            movie_name = self.user_interface.user_input("Enter a movie to add/edit a note for: ")
            movie_note = self.user_interface.user_input("Enter a movie note: ")
            result = self.app_model.add_edit_movie_notes(movie_name, movie_note)
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_message(result)
            self.user_interface.display_movie_notes(movie_notes_list)
        # Calls function to remove from notes list 
        elif action_code == codes.NOTES_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove a note from: ")
            result = self.app_model.remove_movie_note(movie_name)
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_message(result)
            self.user_interface.display_movie_notes(movie_notes_list)
        # Calls function to go to main menu for notes
        elif action_code == codes.NOTES_MAIN:
            self.user_interface.display_main()
        # Calls function to get reviews
        else:
            self.user_interface.display_message("*** Invalid menu option ***")

    def app_is_running(self):
        """Returns status of the app."""
        return self.app_running

    def quit_app(self):
        """Changes status of app to quit."""
        self.app_running = False