class Inventory:
    instance = None
    standards = ["Вода", "Огонь", "Земля", "Воздух"]
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.elements = cls.standards.copy()
        return cls.instance


    def add_element(self, element):
        self.elements.append(element)

    def cleanElements(self):
        def cleanElements(self):
            self.elements.clear()
            self.elements.extend(self.standards)