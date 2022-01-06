from macros.GuardMacro import GuardMacro
from macros.Macro import Macro
from pynput.mouse import Controller as MouseController
from pynput.mouse._xorg import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard._xorg import Controller as KeyboardController
from macros.LeftMouseMacro import LeftMouseMacro
from macros.RightMouseMacro import RightMouseMacro
from macros.Switcher import Switcher
import pyautogui

if __name__ == "__main__":
    mouse: MouseController = MouseController()
    switcher = Switcher()

    macro = Macro(switcher)
    macro.addKeyMacro(switcher)
    macro.addKeyMacro(GuardMacro(mouse))
    macro.addMouseMacro(LeftMouseMacro(mouse, pyautogui))
    macro.addMouseMacro(RightMouseMacro(mouse, pyautogui))

    while True:
        macro.update()