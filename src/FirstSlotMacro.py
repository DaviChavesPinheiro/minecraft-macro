from pynput.keyboard._xorg import KeyCode, Controller

class FirstSlotMacro:
    def __init__(self, keyboard: Controller) -> None:
        self.active = False
        self.keyboard = keyboard

    def on_press(self, args):
        key: KeyCode = args[0]
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