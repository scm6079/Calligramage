import arcade

from src.Calligramage import Calligramage

# Match the core game resolution to the Steam Deck, 1280x800, 16:10
# we will use borders to match the user's desired actual screen resolution
GAME_WIDTH = 1280
GAME_HEIGHT = 800
WINDOW_TITLE = "Calligramage"


def main():
    """ Main method """
    window = Calligramage(GAME_WIDTH, GAME_HEIGHT, WINDOW_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
