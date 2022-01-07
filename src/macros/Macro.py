from pynput import mouse, keyboard

from macros.Switcher import Switcher

class Macro:
    def __init__(self, switcher: Switcher) -> None:
        self.macros = []
        self.switcher = switcher
        
    def update(self):
        if self.switcher.active:
            for macro in self.macros:
                macro.update()
    
    def addMouseMacro(self, object):
        self.macros.append(object)
        mouseListener = mouse.Listener(on_click=lambda x, y, button, pressed: object.on_click(x, y, button, pressed))
        mouseListener.start()
        
    def addKeyMacro(self, object):
        self.macros.append(object)
        self.keyListener = keyboard.Listener(on_press=lambda key: object.on_press(key))
        self.keyListener.start()
        
    
