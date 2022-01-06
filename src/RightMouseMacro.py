from pynput.mouse import Button
from pynput.mouse._xorg import Controller

class RightMouseMacro:
    def __init__(self, mouse: Controller) -> None:
        self.active = False
        self.mouse = mouse

    def on_click(self, args):
        x, y, button, pressed = args
        if button == Button.button8:
            self.active = not self.active
    
    def update(self):
        if self.active:
            self.mouse.click(Button.right, 1)