import arcade
import src.ViewManager as ViewManager
from src.view.AbstractView import AbstractView

MENU_TITLE_FONT_SIZE = 42
MENU_CHOICE_FONT_SIZE = 30
MENU_LINE_HEIGHT = 75
MENU_TOP_PAD = 100
MENU_CENTER_POS = 952
MENU_TOP_POS = 628
WAND_OFFSET_X = 50
WAND_OFFSET_Y = 60


class OptionsView(AbstractView):

    def __init__(self):
        super().__init__()
        self.background = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.PURPLE)
        self.background = arcade.load_texture("resources/images/main-menu.png")

    def on_draw(self):
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.game_width, self.game_height,
                                            self.background)

        arcade.draw_text("Options", self.scaled(MENU_CENTER_POS), self.scaled(MENU_TOP_POS),
                         arcade.color.DEEP_RUBY,
                         font_size=self.scaled(MENU_TITLE_FONT_SIZE), anchor_x="center",
                         font_name="Eagle Lake"
                         )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        ViewManager.show(ViewManager.VIEW_MAIN_MENU)

    def on_key_press(self, key, _modifiers):
        ViewManager.show(ViewManager.VIEW_MAIN_MENU)