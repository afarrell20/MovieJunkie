"""
    Main script to run application
    Acadia Farrell (afarre11)
"""
# Import component classes
from movie_junkie.app_controller import AppController 
from movie_junkie.app_model.app_model import AppModel 
from movie_junkie.user_interface.basic_cli import UserInterface


# Initialize app components 
app_model = AppModel()
user_interface = UserInterface()
app_controller = AppController(app_model=app_model, user_interface=user_interface)


# App runs until user quits
while app_controller.app_running():
    app_controller.next_action()