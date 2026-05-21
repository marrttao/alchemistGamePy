class Inventory:
    instance = None
    standards = ["Вода", "Огонь", "Земля", "Воздух"]
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.elements = []
        return cls.instance


    def add_element(self, element):
        self.elements.append(element)

    def cleanElements(self):
        for element in self.elements:
            element.clean()
            element.append(standarts)