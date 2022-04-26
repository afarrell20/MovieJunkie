"""
    Main script to run application
"""
# Import component classes
from movie_junkie.app_controller import AppController 
from movie_junkie.app_model.app_model import AppModel 
from movie_junkie.user_interface.basic_cli import UserInterface


# Initialize app components 
user_interface = UserInterface()
app_model = AppModel()
app_controller = AppController(user_interface, app_model)

# App runs until user quits
while app_controller.app_running():
    app_controller.next_action()