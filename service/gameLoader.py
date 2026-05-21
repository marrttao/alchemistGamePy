
import json
from models.elements import BunchBuilder, BuildElement


class GameBuilder:
    @staticmethod
    def loadGameData(filepath: str):
        with open(filepath, "r", encoding="utf-8") as file:
           data = json.load(file)
        builder = BunchBuilder()
        elements_pool: dict[str, BuildElement] = {}

        def get_or_create_element(name: str):
            if name not in elements_pool:
                elements_pool[name] = BuildElement(name)
            return elements_pool[name]

        for result_name, ingredients in data.items():

            get_or_create_element(result_name)
            for ingredient_name in ingredients:
                get_or_create_element(ingredient_name)
            builder.add_bunch(result_name, ingredients)

        game_bunch = builder.build()
        return elements_pool, game_bunch

    @staticmethod
    def load(filepath: str):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                return data.get("inventory", [])
        except FileNotFoundError:
            return []

    @staticmethod
    def save(filepath: str, inventory: list[str]):
        with open(filepath, "w") as f:
            json.dump({"inventory": inventory}, f, indent=4)