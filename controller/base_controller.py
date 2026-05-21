from abc import ABC, abstractmethod

from view.interface_view import IRender

from models.inventory import Inventory
from service.gameLoader import GameBuilder


class BaseController(ABC):
    def __init__(self, view: IRender):
        self._view = view
        self.inventory = Inventory()

        self.all_elements, self.bunch = GameBuilder.loadGameData("gamedata/bunches_of_elements.json")

    @abstractmethod
    def start(self):
        pass

    def save_game(self):
        GameBuilder.save("gamedata/save.json", self.inventory.elements)
        self._view.draw_text(f"Successfully saved!")

    def load_game(self):
        loaded_elements = GameBuilder.load("gamedata/save.json")

        if loaded_elements:
            self.inventory.elements = loaded_elements
            self._view.draw_text(f"Successfully loaded!")
        else:
            self.view.draw_text(f"Failed to load!")

    def try_combine(self, elements: list[str]):
        ingredients = [item.strip().lower() for item in elements]

        for item in elements:
            if item not in self.inventory.elements:
                self._view.draw_text(f"You don't have {item} in inventory")
                return False

        elements_sorted = sorted(elements)
        recipe_found = False

        for result, recipe in self.bunch.diary.items():
            if elements_sorted == sorted(recipe):
                recipe_found = True

                if result not in self.inventory.elements:
                    self.inventory.add_element(result)
                    self._view.draw_text(f"You have created {result}!")
                    self.check_the_story_chapter(result)
                    return True
                else:
                    self._view.draw_text(f"Successfully combined into {result}... but you already discovered it earlier. Try another combination!")
                    return False

        if not recipe_found:
            self._view.draw_text(f"This combination is total rubbish!")
            return False
        return None

    def check_the_story_chapter(self, element: str):
        match element:
            case "Life": self._view.draw_text(f"You have created Life! The world is no longer empty")
            case "Human": self._view.draw_text(f"You have created Human! Intelligence is true power")
            case "Cyborg": self._view.draw_text(f"You have created Cyborg! The end of evolution!")