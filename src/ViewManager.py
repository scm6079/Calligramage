# Import all the views and provide a way to get them by name
from src.view.MainMenuView import MainMenuView
from src.view.OptionsView import OptionsView
from src.view.CinematicIntroView import CinematicIntroView
from src.view.GameView import GameView
# from src.view.LoadGameView import LoadGameView
# from src.view.SaveGameView import SaveGameView
# from src.view.GameOverView import GameOverView
# from src.view.GameWonView import GameWonView
# from src.view.CreditsView import CreditsView
# from src.view.PauseView import PauseView
# from src.view.LevelSelectView import LevelSelectView
# from src.view.LevelCompleteView import LevelCompleteView
# from src.view.LevelFailedView import LevelFailedView

active_view = None
arcade_window = None

VIEW_MAIN_MENU = "main_menu"
VIEW_OPTIONS = "options"
VIEW_CINEMATIC_INTRO = "cinematic_intro"
VIEW_GAME = "game"
VIEW_LOAD_GAME = "load_game"
VIEW_SAVE_GAME = "save_game"
VIEW_GAME_OVER = "game_over"
VIEW_GAME_WON = "game_won"
VIEW_CREDITS = "credits"
VIEW_PAUSE = "pause"
VIEW_LEVEL_SELECT = "level_select"
VIEW_LEVEL_COMPLETE = "level_complete"
VIEW_LEVEL_FAILED = "level_failed"


# TODO: finish the implementation of the view stubs listed here
def show(view_name):
    global active_view

    if view_name == VIEW_MAIN_MENU:
        view = MainMenuView()
    elif view_name == VIEW_OPTIONS:
        view = OptionsView()
    elif view_name == VIEW_CINEMATIC_INTRO:
        view = CinematicIntroView()
    elif view_name == VIEW_GAME:
        view = GameView()
    # elif view_name == VIEW_LOAD_GAME:
    #    view = LoadGameView()
    # elif view_name == VIEW_SAVE_GAME:
    #    view = SaveGameView()
    # elif view_name == VIEW_GAME_OVER:
    #    view = GameOverView()
    # elif view_name == VIEW_GAME_WON:
    #    view = GameWonView()
    # elif view_name == VIEW_CREDITS:
    #    view = CreditsView()
    # elif view_name == VIEW_PAUSE:
    #    view = PauseView()
    # elif view_name == VIEW_LEVEL_SELECT:
    #    view = LevelSelectView()
    # elif view_name == VIEW_LEVEL_COMPLETE:
    #     view = LevelCompleteView()
    # elif view_name == VIEW_LEVEL_FAILED:
    #     view = LevelFailedView()
    else:
        raise ValueError(f"Unknown view name: {view_name}")

    arcade_window.show_view(view)
    active_view = view_name

