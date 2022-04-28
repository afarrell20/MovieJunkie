"""
    App controller component acts as core of application. It handles processing of user input from the 
    user interface and acts on the model if applicable. Also responsible for interacting with and
    updating user interface. 
    
    Author: Maggie Whittier (mewhiiti)
"""
import movie_junkie.user_interface.interface_codes as codes


class AppController:
    def __init__(self, model, user_interface):
        self.model = model 
        self.user_interface = user_interface
        self.app_running = True
        self.user_interface.display_title()
        self.user_interface.display_main()

    def next_action(self):
        """Get user input from user interface and process the input to execute the 
           associated action."""
        pass

    def app_is_running(self):
        """Returns status of the app."""
        return self.app_running

    def quit_app(self):
        """Changes status of app to quit."""
        self.app_running = False
