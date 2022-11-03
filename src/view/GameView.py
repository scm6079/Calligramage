import arcade
from src.view.AbstractView import AbstractView


class GameView(AbstractView):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Calligramage gameplay view", self.game_width / 2, self.game_height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
