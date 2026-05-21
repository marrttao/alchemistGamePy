from interface_view import IRender

class ConsoleView(IRender):
    def _draw_elements(self, recipe):
        recipe_length = len(recipe)

        for item_index in recipe_length:
            print(recipe[item_index])

            if recipe_length != item_index + 1:
                print(" + ")

    def draw_text(self, message: str):
        print(f"{message}")

    def draw_recipe(self, result: str, recipe: list[str]):
        print(f"{result} = ")
        self._draw_elements(recipe)

    def draw_bunch(self, bunch: dict[str, list[str]]):
        for result, recipe in bunch.items():
            print(f"{result} = ")
            self._draw_elements(recipe)