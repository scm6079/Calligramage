import arcade
import os


class Calligramage(arcade.Window):
    def __init__(self, width, height, title):
        """ Set up the class. """
        super().__init__(width, height, title, resizable=True)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Physics engine
        self.physics_engine = None

        # TODO: Complete any other initialization we need

    def setup(self):
        """ Create game items """
        # Create the physics engine
        # self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Draw everything. """
        self.clear()
        arcade.draw_text("Calligramage", 10, 10, arcade.color.WHITE, 14)

    def on_resize(self, width, height):
        """ User resizes the screen. """

    def on_key_press(self, key, _):
        """A key is pressed. """

    def on_key_release(self, key, _):
        """The user releases a key. """

    def scroll_screen(self):
        """ Manage Scrolling """

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        # self.physics_engine.update()
