from Macro import Macro
from pynput.mouse import Controller
from pynput.mouse._xorg import Controller
from LeftMouseMacro import LeftMouseMacro
from Switcher import Switcher

if __name__ == "__main__":
    mouse: Controller = Controller()
    switcher = Switcher()

    macro = Macro(switcher)
    macro.addKeyMacro(switcher)
    macro.addMouseMacro(LeftMouseMacro(mouse))

    while True:
        macro.update()