import keyboard as key
import pyautogui as gui
import time

#change pyautogui delay to mash faster
gui.PAUSE = 0.001

def get_lead_out(sleep_seconds):
    time.sleep(sleep_seconds)

    start_time = time.time()
    while time.time() - start_time <= 15:
        if key.is_pressed('q'):
            exit(0)
        gui.keyDown('x')
        gui.keyUp('x')

get_lead_out(5)

#change pyautogui delay back
gui.PAUSE = 0.1