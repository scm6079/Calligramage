import arcade
import pyglet
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


class MainMenuView(AbstractView):

    def __init__(self):
        super().__init__()
        self.background = None
        self.emitter = None
        self.soundPlayer = None
        self.emitter_timeout = 0
        self.selected = 0

    def create_wand_emitter(self):
        center = self.game_width / 2 + self.scaled(WAND_OFFSET_X), self.game_height / 2 + self.scaled(WAND_OFFSET_Y)
        return arcade.Emitter(
            center_xy=center,
            emit_controller=arcade.EmitInterval(0.02),
            particle_factory=lambda emitter: arcade.LifetimeParticle(
                filename_or_texture=":resources:images/pinball/pool_cue_ball.png",
                lifetime=8.0,
                change_xy=arcade.rand_in_circle((0.0, 0.0), 1.0),
                scale=self.scaled(0.3),
                alpha=32
            )
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.PURPLE)
        # Load the background image
        self.background = arcade.load_texture("resources/images/main-menu.png")
        self.emitter = self.create_wand_emitter()
        sound = arcade.load_sound("resources/sounds/MainMenu.wav", True)
        self.soundPlayer = arcade.play_sound(sound, volume=0.8, looping=True)

    def on_hide_view(self):
        arcade.stop_sound(self.soundPlayer)
        self.emitter = None

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.emitter = self.create_wand_emitter()

    def draw_menu_choice(self, text, fullSize, count):
        y_unscaled = MENU_TOP_POS - MENU_TOP_PAD - (count * MENU_LINE_HEIGHT)
        # Set the color based on if it's selected or not
        active = self.selected == count
        if active:
            color = arcade.color.BLACK
            arcade.draw_circle_filled(self.scaled(MENU_CENTER_POS - fullSize), self.scaled(y_unscaled)+self.scaled(12),
                                      self.scaled(10), color)
            arcade.draw_line(self.scaled(MENU_CENTER_POS - fullSize - 40), self.scaled(y_unscaled) + self.scaled(12),
                             self.scaled(MENU_CENTER_POS - fullSize), self.scaled(y_unscaled) + self.scaled(12),
                             color, self.scaled(2))
            arcade.draw_circle_filled(self.scaled(MENU_CENTER_POS + fullSize),
                                      self.scaled(y_unscaled) + self.scaled(12),
                                      self.scaled(10), color)
            arcade.draw_line(self.scaled(MENU_CENTER_POS + fullSize), self.scaled(y_unscaled) + self.scaled(12),
                             self.scaled(MENU_CENTER_POS + fullSize + 40), self.scaled(y_unscaled) + self.scaled(12),
                             color, self.scaled(2))
        else:
            color = arcade.color.GRAY

        arcade.draw_text(text, self.scaled(MENU_CENTER_POS), self.scaled(y_unscaled),
                         color,
                         font_size=self.scaled(MENU_CHOICE_FONT_SIZE), anchor_x="center",
                         font_name="Eagle Lake"
                         )

    def update(self, delta_time):
        if self.emitter:
            self.emitter_timeout += 1
            self.emitter.update()

    def on_draw(self):
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.game_width, self.game_height,
                                            self.background)

        arcade.draw_text("Main Menu", self.scaled(MENU_CENTER_POS), self.scaled(MENU_TOP_POS),
                         arcade.color.DEEP_RUBY,
                         font_size=self.scaled(MENU_TITLE_FONT_SIZE), anchor_x="center",
                         font_name="Eagle Lake"
                         )

        self.draw_menu_choice("New Game", 150, 0)
        self.draw_menu_choice("Load Game", 160, 1)
        self.draw_menu_choice("Options", 120, 2)
        self.draw_menu_choice("Quit", 80, 3)

        # Draw the emitter related stuff
        if self.emitter:
            self.emitter.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # If the user presses the mouse button, go to the menu choice they clicked.
        # TODO: Figure out if the user clicked on the "New Game" button
        ViewManager.show(ViewManager.VIEW_CINEMATIC_INTRO)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.UP:
            self.selected -= 1
        elif key == arcade.key.DOWN:
            self.selected += 1

        if self.selected < 0:
            self.selected = 3
        elif self.selected > 3:
            self.selected = 0

        if key == arcade.key.ENTER:
            if self.selected == 0:
                ViewManager.show(ViewManager.VIEW_CINEMATIC_INTRO)
            elif self.selected == 1:
                print("Load Game")
            elif self.selected == 2:
                print("Options")
            elif self.selected == 3:
                pyglet.app.exit()
