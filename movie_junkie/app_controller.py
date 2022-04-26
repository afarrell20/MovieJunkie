"""
    App controller component acts as core of application. It handles processing of user input from the 
    user interface and acts on the model if applicable. Also responsible for interacting with and
    updating user interface. 
    
    Author: Acadia Farrell (afarre11)
"""
class AppController:
    def __init__(self, model, user_interface):
        self.app_running = True
        self.model = model 
        self.user_interface = user_interface
        self.user_interface.display_title()
        self.user_interface.display_main()

    def next_action():
        """Get user input from user interface and process the input to execute the 
           associated action"""
        pass

    def app_running():
        """Returns status of the app"""
        return self.app_running

    def quit_app():
        """Changes status of app to quit"""
        self.app_running = False
