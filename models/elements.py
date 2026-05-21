from abc import ABC, abstractmethod

class Element(ABC):
    def __init__(self, name,):
        self.name = name

    @abstractmethod
    def get_name(self):
        pass

class BuildElement(Element):
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return self


class Bunch:
    def __init__(self):
        self.diary: dict[str, list[str]] = {}

    def show(self):
        for result, recipe in self.diary.items():
            formula = ""
            for i in range(len(recipe)):
                formula += recipe[i]
                if i < len(recipe) - 1:
                    formula += " + "


class BunchBuilder:
    def __init__(self):
        self._bunch = Bunch()

    def add_bunch(self, result: str, recipe: list[str]):
        self._bunch.diary[result] = recipe
        return self

    def build(self) -> Bunch:
        return self._bunch


class BuildGameData(Element):
    def get_name(self):
        return self.name
