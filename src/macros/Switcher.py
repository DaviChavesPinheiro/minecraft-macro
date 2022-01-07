from pynput.keyboard._xorg import KeyCode

class Switcher:
    def __init__(self) -> None:
        self.active = False

    def on_press(self, key: KeyCode):
        try:
            if key.char == ']':
                self.active = not self.active
                if(self.active):
                    print("Macro activated")
                else:
                    print("Macro disabled")
        except AttributeError:
            None
    
    def update(self):
        pass