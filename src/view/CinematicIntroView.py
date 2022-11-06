import arcade
import src.ViewManager as ViewManager
from src.view.AbstractView import AbstractView


class CinematicIntroView(AbstractView):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.YELLOW)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Intro Placeholder", self.game_width / 2, self.game_height / 2,
                         arcade.color.BLACK, font_size=self.scaled(50), anchor_x="center")
        arcade.draw_text("Click to start game", self.game_width / 2, self.game_height / 2 - self.scaled(75),
                         arcade.color.GRAY, font_size=self.scaled(20), anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        ViewManager.show(ViewManager.VIEW_GAME)
