import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

#key to set the autoclicker to on/off.
TOOGLE_KEY = KeyCode(char="p")

#normal state of condition (false, the autoclicker is off)
clicking = False
mouse = Controller()

#activate autoclicker
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001)

#deactivate clicker
def toggle_event(key):
    if key == TOOGLE_KEY:
        global clicking
        clicking = not clicking

click_thred = threading.Thread(target=clicker)
click_thred.start()

with Listener(on_press=toggle_event) as Listener:
    Listener.join()