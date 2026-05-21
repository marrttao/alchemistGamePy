import sys

from ConsoleView import console_view
from GuiView import gui_view

from controller.console_controller import ConsoleController
from controller.gui_controller import GuiController

def run(args):
    view = ConsoleView()
    game_controller = ConsoleController(view)

    if len(args) > 1 and args[1] == "--gui":
        view = GuiView()
        game_controller = GameController(view)

    game_controller.start()

if __name__ == "__main__":
    run(sys.argv)