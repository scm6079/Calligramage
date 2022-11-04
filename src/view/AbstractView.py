import arcade

# Match the core game resolution to the Steam Deck, 1280x800, 16:10
# we will use borders to match the user's desired actual screen resolution
GAME_WIDTH = 1280
GAME_HEIGHT = 800


class AbstractView(arcade.View):
    active_scale = 1.0

    def __init__(self):
        super().__init__()

    # Get the game board width, which is the raw game resolution minus the borders and any scaling
    # This is the actual game board width size in pixels, not the window size
    @property
    def game_width(self):
        return self.scaled(GAME_WIDTH)

    # Get the game board height, which is the raw game resolution minus the borders and any scaling
    # This is the actual game board height size in pixels, not the window size
    @property
    def game_height(self):
        return self.scaled(GAME_HEIGHT)

    # Get the active game scale, which defaults to 1.0, but may be changed by the user
    @property
    def game_scale(self):
        return AbstractView.active_scale

    def on_resize(self, width, height):
        super().on_resize(width, height)
        AbstractView.active_scale = width / GAME_WIDTH

    # Get a scaled element size, which is the game scale multiplied by the element size
    def scaled(self, value):
        return value * self.game_scale
