import arcade

# Match the core game resolution to the Steam Deck, 1280x800, 16:10
# we will use borders to match the user's desired actual screen resolution
GAME_WIDTH = 1280
GAME_HEIGHT = 800


class AbstractView(arcade.View):

    # Get the game board width, which is the raw game resolution minus the borders and any scaling
    # At the moment, this is fixed, but this may become dynamic in the future, so this method should always
    # be used to get the game board width
    @property
    def game_width(self):
        return GAME_WIDTH

    # Get the game board height, which is the raw game resolution minus the borders and any scaling
    # At the moment, this is fixed, but this may become dynamic in the future, so this method should always
    # be used to get the game board height
    @property
    def game_height(self):
        return GAME_HEIGHT
