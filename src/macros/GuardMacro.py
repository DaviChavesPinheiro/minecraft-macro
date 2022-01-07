from pynput import mouse
from pynput.keyboard._xorg import KeyCode
from pynput.keyboard import Key
import pyautogui

class GuardMacro:
    def __init__(self,  mouse: pyautogui) -> None:
        self.active = False
        self.mouse = mouse

    def on_press(self, key: KeyCode):
        try:
            if key == Key.alt:
                self.active = not self.active
        except AttributeError:
            None
    
    def update(self):
        if self.active:
            self.mouse.move(1, 0)