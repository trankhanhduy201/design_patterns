from abc import ABC, abstractmethod

# Abstract products
class Button(ABC):
    @abstractmethod
    def click(self): pass

class Checkbox(ABC):
    @abstractmethod
    def check(self): pass

# Concrete products for Windows
class WinButton(Button):
    def click(self):
        print("Windows Button clicked.")

class WinCheckbox(Checkbox):
    def check(self):
        print("Windows Checkbox checked.")

# Concrete products for Mac
class MacButton(Button):
    def click(self):
        print("Mac Button clicked.")

class MacCheckbox(Checkbox):
    def check(self):
        print("Mac Checkbox checked.")

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass
    
    @abstractmethod
    def create_checkbox(self): pass

# Concrete factories
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client code
def build_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.click()
    checkbox.check()

# Usage
print("Building Windows UI:")
build_ui(WinFactory())

print("\nBuilding Mac UI:")
build_ui(MacFactory())
