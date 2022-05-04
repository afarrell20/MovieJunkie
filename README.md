# Movie Junkie
As avid movie watchers, we understand the importance of tracking your movie watching history. We decided that we needed a way to keep track of the movies we have and have not seen. This knowledge was not enough for us, however. There also needs to be a way to keep track of movie notes and our own personal reviews for movies that we have seen. We also wanted to be able to access movie reviews and reccomendations from imbd. 

## Install Required Packages
Navigate to the main MovieJunkie directory (not movie_junkie) and run:

    pip install -r requirements.txt

## Run Movie Junkie
Must be connected to wifi for full features. Navigate to the main MovieJunkie directory (not movie_junkie) and run:
    
    python (or python3) movie_junkie.py

## App Model
    -Import the imbd and pickle.
    -Get user data.
    -Stores and interacts with the app data.
    -Interacts with the app controller.
    -Called in app controller based on user input from menu selection.
    
## User Interface
    -Menu is being displayed.
    -Imput is gathered and data interacts with the app controller.
    -Controlled by app controller to display content resquested by the user.
    -Pretty print function formates the data in a neat format.
        -Display_main
            -6 menu options.
            -Each menu option has a related code that display a new menu when imputed.
        -Display want_to_watch
            -When user selects 1 from the main menu.
            -3 menu options.
        -Display have_watched
            -When user selects 2 from the main menu.
            -3 menu options.
        -Display movie_reviews
            -When user selects 4 from the main menu
            -No menu options.
            -Print review based on user imput.
            -Bring user back to main menu
        -Get movie reccomendations 
            -No menu options
            -When user selects 5 from the main menu.
            -Prints reccomendation based on user imput
            -Bring user back to main menu. 

## App Controller
    -Core of app.
    -Process user imput from the basic_cli.
    -Calls the correct function from the app model.
    -Interacts with the user.
    -Updates the interface.
    -App Controller class calls the app model and user interface.
        -Next action:
            -Get imput from the user and process that information.
            -Action code is what the user imputs.
            -Relates to the interface codes.
            -Depending on what code is entered it calls a option from app model and display correct title from basic_cli.
    -Keeps running as long as the quit option is returned true. 
        -Keywords for reccomendations
            -Keyword specific
                -Ex: psychological-thriller, slapstick-comedy, romantic-comedy, historical-fiction, action-hero, dark-comedy, slasher-horror.

## movie_junkie.py
    -Main function.
    -Imports the classes.
    -Intalize the app component for the classes.
    -Get the boolean from the app controller for the while statement.
    -If returned true it will keep cycling through next action.
    -If returned false it will stop the action. 

## Citations 
    McConnell, S. (2004). Code complete (Second). Microsoft Press. 

    Pickle - Python object serialization¶. pickle - Python object serialization - Python 3.10.4 documentation. (n.d.). Retrieved April 29, 2022, from https://docs.python.org/3/library/pickle.html

    Python classes and objects. Python Classes. (n.d.). Retrieved April 29, 2022, from https://www.w3schools.com/python/python_classes.asp

    Usage. Usage - Cinemagoer 6.8 documentation. (n.d.). Retrieved April 29, 2022, from https://cinemagoer.readthedocs.io/en/latest/usage/index.html

    Farrell, Alex, et al. “Design Help and Code Insight.” 27 Apr. 2022. 