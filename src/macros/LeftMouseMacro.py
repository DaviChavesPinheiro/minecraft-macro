from pynput.mouse import Button
from pynput.mouse._xorg import Controller as MouseController
import pyautogui
from time import sleep
class LeftMouseMacro:
    def __init__(self, mouse: MouseController, keyboard: pyautogui) -> None:
        self.active = False
        self.mouse = mouse
        self.keyboard = keyboard

    def on_click(self, x, y, button, pressed):
        if button == Button.button9:
            self.active = not self.active
            if pressed:
                self.keyboard.press('1')

    def update(self):
        if self.active:
            self.mouse.click(Button.left, 1)
        