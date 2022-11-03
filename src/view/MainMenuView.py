import arcade
from src.view.AbstractView import AbstractView
from src.view.CinematicIntroView import CinematicIntroView


class MainMenuView(AbstractView):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Menu Screen", self.game_width / 2, self.game_height / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.game_width / 2, self.game_height / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(CinematicIntroView())
