from controller.base_controller import BaseController

class ConsoleController(BaseController):
    def start(self):
        self._view.draw_text("Welcome! (commands: exit, save, load)")

        while True:
            self._view.draw_text(f"Your inventory: ")
            for element in self.inventory.elements:
                self._view.draw_text(f"{element} ")

            command = input("\nEnter 2 or more elements, separated by space or command: ").strip()

            match command.lower():
                case "exit": break
                case "save":
                    self.save_game()
                    continue
                case "load":
                    self.load_game()
                    continue

            ingredients = command.split()
            if len(ingredients) < 2:
                self._view.draw_text(f"You must enter at least 2 ingredients!")
                continue

            self.try_combine(ingredients)