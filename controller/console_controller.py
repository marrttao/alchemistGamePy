from controller.base_controller import BaseController

class ConsoleController(BaseController):
    def start(self):
        self._view.draw_text("Welcome! (enter 'exit' to exit)")
        self._view.draw_text(self.inventory.elements)

        while True:
            command = input("\nEnter 2 or more elements, separated by space: ").strip()

            if command == "exit": break

            ingredients = command.split()
            if len(ingredients) < 2:
                self._view.draw_text(f"You must enter at least 2 ingredients!")
                continue

            self.try_combine(ingredients)