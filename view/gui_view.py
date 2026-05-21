from interface_view import IRender

class GuiView(IRender):
    def __there_is_no_gui(self):
        print("GUI is not implemented yet")

    def draw_recipe(self, result: str, recipe: list[str]):
        self.__there_is_no_gui()

    def draw_error(self, message: str):
        self.__there_is_no_gui()

    def draw_bunch(self, bunch: dict[str, list[str]]):
        self.__there_is_no_gui()