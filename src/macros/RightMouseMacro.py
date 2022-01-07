from pynput.mouse import Button
from pynput.mouse._xorg import Controller as MouseController
from pynput.keyboard._xorg import Controller as KeyboardController
import pyautogui
class RightMouseMacro:
    def __init__(self, mouse: MouseController, keyboard: pyautogui) -> None:
        self.active = False
        self.mouse = mouse
        self.keyboard = keyboard

    def on_click(self, x, y, button, pressed):
        if button == Button.button8:
            self.active = not self.active
            if pressed:
                self.keyboard.press('8')

    def update(self):
        if self.active:
            self.mouse.click(Button.right, 1)