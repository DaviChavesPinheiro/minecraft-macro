from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import pyautogui

mouseController = Controller()

def on_click(x, y, button, pressed):
    if button == Button.button9:
        global isLeftClickMacroActived
        isLeftClickMacroActived = not isLeftClickMacroActived

def on_press(key):
    try:
        if key.char == ']':
            global isMacroActived
            isMacroActived = not isMacroActived
            if(isMacroActived):
                print("Macro activated")
            else:
                print("Macro disabled")
    except AttributeError:
        None

mouseListener = mouse.Listener(on_click=on_click)
mouseListener.start()

keyboardListener = keyboard.Listener(on_press=on_press)
keyboardListener.start()

isMacroActived = False
isLeftClickMacroActived = False
while True:
    if isMacroActived:
        if isLeftClickMacroActived:
            mouseController.click(Button.left, 1)

            

