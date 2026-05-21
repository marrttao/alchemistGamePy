from abc import ABC, abstractmethod

class IRender(ABC):
    @abstractmethod
    def draw_text(self, message: str):
        pass

    @abstractmethod
    def draw_recipe(self, result: str, recipe: list[str]):
        pass

    @abstractmethod
    def draw_bunch(self, bunch: dict[str, list[str]]):
        pass