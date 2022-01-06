from pynput import mouse, keyboard

from EventManager import EventManager
from Switcher import Switcher

class Macro:
    def __init__(self, switcher) -> None:
        self.onMouseEvents = EventManager()
        self.onKeyEvents = EventManager()
        self.macros = []
        self.switcher: Switcher = switcher

        self.mouseListener = mouse.Listener(on_click=lambda x, y, button, pressed: self.onMouseEvents.notify(lambda obj: obj.on_click, x, y, button, pressed))
        self.mouseListener.start()

        self.keyListener = keyboard.Listener(on_press=lambda key: self.onKeyEvents.notify(lambda obj: obj.on_press, key))
        self.keyListener.start()
    def update(self):
        if self.switcher.active:
            for macro in self.macros:
                macro.update()
    
    def addMouseMacro(self, object):
        self.macros.append(object)
        self.onMouseEvents.subscribe(object)
        
    def removeMouseMacro(self, object):
        self.macros.remove(object)
        self.onMouseEvents.unsubscribe(object)

    def addKeyMacro(self, object):
        self.macros.append(object)
        self.onKeyEvents.subscribe(object)
        
    def removeKeyMacro(self, object):
        self.macros.remove(object)
        self.onKeyEvents.unsubscribe(object)

    
