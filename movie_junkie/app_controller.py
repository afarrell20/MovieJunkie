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
        
        # Calls user input from user interface class
        if action_code == codes.MAIN_HAVE:
            have_watched_list = self.app_model.get_have_watched()
            self.user_interface.display_have_watch(have_watched_list)
        elif action_code == codes.MAIN_NOTES:
            pass
        elif action_code == codes.MAIN_REVIEWS:
            pass
        elif action_code == codes.MAIN_RECOMMENDATIONS:
            pass
        elif action_code == codes.MAIN_QUIT:
            self.app_model.save_data()
            self.user_interface.display_message("*** Thank you for using MovieJunkie ***")
            self.quit_app()
        elif action_code == codes.WANT:
            pass
        elif action_code == codes.WANT_WATCH_ADD:
            movie_name = self.user_interface.user_input("Enter a movie name: ")
            result = self.app_model.add_movie_want_watch(movie_name)
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch()
        elif action_code == codes.WANT_WATCH_REMOVE:
            movie_name = self.user_interface.user_input("Enter a movie to remove: ")
            result = self.app_model.remove_movie_want_watch(movie_name)
            self.user_interface.display_message(result)
            self.user_interface.display_want_watch()
        elif action_code == codes.WANT_WATCH_MAIN:
            pass
        elif action_code == codes.HAVE_WATCHED_ADD:
            pass
        elif action_code == codes.HAVE_WATCHED_REMOVE:
            pass
        elif action_code == codes.HAVE_WATCHED_MAIN:
            pass
        elif action_code == codes.NOTES_ADD:
            pass
        elif action_code == codes.NOTES_REMOVE:
            pass
        elif action_code == codes.NOTES_MAIN:
            pass
        elif action_code == codes.REVIEWS_GET:
            pass
        elif action_code == codes.REVIEWS_MAIN:
            pass
        elif action_code == codes.RECOMMENDATIONS_GET:
            pass
        elif action_code == codes.RECOMMENDATIONS_MAIN:
            pass
        else:
            self.user_interface.display_message("*** Invalid menu option **")


        

    #Example if user is on main and enters option to go to have watched list menu:
    # if input = codes.MAIN_HAVE:
    #   have_watched_list = app_model.get_have_watched()
    #   user_interface.display_have_watch(have_watched_list)
    # Now user clicks add movie in this menu:
    # elif input = codes.HAVE_WATCHED_ADD:
    #   movie_name = user_interface.user_input("Enter movie title: ")   
    #   result = app_model.add_movie_have_watched(movie_name)
    #   user_interface.display_message(result)
    #    have_watched_list = app_model.get_have_watched()
    #   user_interface.display_have_watched(have_watched_list)

    def app_is_running(self):
        """Returns status of the app."""
        return self.app_running

    def quit_app(self):
        """Changes status of app to quit."""
        self.app_running = False
