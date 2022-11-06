import arcade
import os
import src.ViewManager as ViewManager

# Our "launcher" size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Calligramage"


# Core window management class
class Calligramage:

    def __init__(self):
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in.
        self.window = None
        self.active_view = None
        file_path = os.path.dirname(os.path.abspath(__file__))
        parent_path = (os.path.abspath(os.path.join(file_path, os.pardir)))
        os.chdir(parent_path)

    def init_resources(self):
        """ Initialize fonts, sounds, and views """
        arcade.load_font("resources/fonts/EagleLake-Regular.ttf")
        ViewManager.arcade_window = self.window

    def show_view(self, view):
        self.active_view = view
        self.active_view.setup()
        self.window.show_view(self.active_view)

    def run(self):
        """ Run game """
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        self.init_resources()
        ViewManager.show(ViewManager.VIEW_MAIN_MENU)
        arcade.run()
