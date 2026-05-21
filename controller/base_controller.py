from abc import ABC, abstractmethod

from interface_view import IRender

from models.inventory import Inventory
from service.gameLoader import GameBuilder


def BaseController(ABC):
    def __init__(self, view: IRender):
        self._view = view
        self.inventory = Inventory()

        self.all_elements, self.bunch = GameBuilder.loadGameData("gamedata/bunches_of_elements.json")

    @abstractmethod
    def start(self):
        pass

    def try_combine(self, elements: list[str]):
        for item in elements:
            if item not in self.inventory.elements:
                self._view.draw_text(f"You don't have {item} in inventory")
                return

        elements_sorted = sorted(self.elements)
        recipe_found = False

        for result, recipe in self.bunch.diary.items():
            if elements_sorted == sorted(recipe):
                recipe_found = True

                if self.inventory.add_element(result):
                    self._view.draw_recipes(result, recipe)
                    self._view.draw_text(f"You have created {result}!")
                else:
                    self._view.draw_text(f"Successfully combined into {result}... but you already discovered it earlier. Try another combination!")
                break

        if not recipe_found:
            self.view.draw_text(f"This combination is total rubbish!")