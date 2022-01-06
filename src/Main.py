from Macro import Macro
from pynput.mouse import Controller as MouseController
from pynput.mouse._xorg import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard._xorg import Controller as KeyboardController
from LeftMouseMacro import LeftMouseMacro
from RightMouseMacro import RightMouseMacro
from Switcher import Switcher
import pyautogui

if __name__ == "__main__":
    mouse: MouseController = MouseController()
    keyboard: pyautogui = pyautogui
    switcher = Switcher()

    macro = Macro(switcher)
    macro.addKeyMacro(switcher)
    macro.addMouseMacro(LeftMouseMacro(mouse, keyboard))
    macro.addMouseMacro(RightMouseMacro(mouse, keyboard))

    while True:
        macro.update()