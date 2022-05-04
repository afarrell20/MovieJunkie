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
        action_code = self.user_interface.user_input("\n>>> ")
        
        # User on Main Menu, selects to go to Want to Watch Menu
        if action_code == codes.MAIN_WANT:
            want_watch_list = self.app_model.get_want_watch()
            self.user_interface.display_want_watch(want_watch_list)
        # User on Main Menu, selects to go to Have Watched Menu  
        elif action_code == codes.MAIN_HAVE:
            have_watched_list = self.app_model.get_have_watched()
            self.user_interface.display_have_watch(have_watched_list)
        # User on Main Menu, selects to go to Movie Notes Menu
        elif action_code == codes.MAIN_NOTES:
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_movie_notes(movie_notes_list)
        # User on Main Menu, selects to get movie review
        elif action_code == codes.MAIN_REVIEWS:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            reviews = self.app_model.get_movie_reviews(movie_name)
            self.user_interface.display_movie_reviews(reviews)
        # User on Main Menu, selects to get movie recommendations
        elif action_code == codes.MAIN_RECOMMENDATIONS:
            keyword = self.user_interface.user_input("Enter a movie keyword (ex: slapstick-comedy): ")
            recommendations = self.app_model.get_movie_recommendations(keyword)
            self.user_interface.display_movie_recommendations(recommendations)
        # User on Main Menu, selects to quit app
        elif action_code == codes.MAIN_QUIT:
            self.app_model.save_data()
            self.user_interface.display_message("*** Thank you for using MovieJunkie ***")
            self.quit_app()
        # User on Want to Watch Menu, selects to add movie to the list
        elif action_code == codes.WANT_WATCH_ADD:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            result = self.app_model.add_movie_want_watch(movie_name)
            movie_list = self.app_model.get_want_watch()
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch(movie_list)
        # User on Want to Watch Menu, selects to remove movie from the list
        elif action_code == codes.WANT_WATCH_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove: ")
            result = self.app_model.remove_movie_want_watch(movie_name)
            movie_list = self.app_model.get_want_watch()
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch(movie_list)
        # User on Want to Watch Menu, selects to go back to Main Menu
        elif action_code == codes.WANT_WATCH_MAIN:
            self.user_interface.display_main()
         # User on Have Watched Menu, selects to add movie to the list
        elif action_code == codes.HAVE_WATCHED_ADD:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            result = self.app_model.add_movie_have_watched(movie_name)
            movie_list = self.app_model.get_have_watched()
            self.user_interface.display_message(result)
            self.user_interface.display_have_watch(movie_list) 
        # User on Have Watched Menu, selects to remove movie from the list 
        elif action_code == codes.HAVE_WATCHED_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove: ")
            result = self.app_model.remove_movie_have_watched(movie_name)
            movie_list = self.app_model.get_have_watched()
            self.user_interface.display_message(result)
            self.user_interface.display_have_watch(movie_list)
        # User on Have Watched Menu, selects to go back to Main Menu
        elif action_code == codes.HAVE_WATCHED_MAIN:
            self.user_interface.display_main()
        # User on Movie Notes Menu, selects to add note to the list
        elif action_code == codes.NOTES_ADD:
            movie_name = self.user_interface.user_input("Enter a movie to add/edit a note for: ")
            movie_note = self.user_interface.user_input("Enter a movie note: ")
            result = self.app_model.add_edit_movie_notes(movie_name, movie_note)
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_message(result)
            self.user_interface.display_movie_notes(movie_notes_list)
        # User on Movie Notes Menu, selects to remove note from the list 
        elif action_code == codes.NOTES_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove a note from: ")
            result = self.app_model.remove_movie_note(movie_name)
            movie_notes_list = self.app_model.get_movie_notes()
            self.user_interface.display_message(result)
            self.user_interface.display_movie_notes(movie_notes_list)
        # User on Movie Notes Menu, selects to go back to Main Menu
        elif action_code == codes.NOTES_MAIN:
            self.user_interface.display_main()
        # User enters invalid menu choice
        else:
            self.user_interface.display_message("*** Invalid menu option ***")

    def app_is_running(self):
        """Returns status of the app."""
        return self.app_running

    def quit_app(self):
        """Changes status of app to quit."""
        self.app_running = False