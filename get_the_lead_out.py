#get the lead out has the players mash a button to get lead out of a mechanical pencil as fast as possible
#for some reason there is an acceleration system where you dont push lead out when button is pressed, but rather at a rate that goes up when you mash

import keyboard as key
import pyautogui as gui
import time
import pygetwindow as gw

def get_lead_out():
    #change pyautogui delay to mash faster
    gui.PAUSE = 0.001
    
    # switch to emulator
    emulator_window = gw.getWindowsWithTitle("DeSmuME")[0]
    emulator_window.activate()

    #delay the program starting to not mash early and mess up any menuing or switching to game window
    time.sleep(2)

    start_time = time.time()
    while time.time() - start_time <= 15:
        #emergency escape key since it is bound to left shoulder, which is not used for any minigames
        if key.is_pressed('q'):
            exit(0)
        #mash the 'a button' in the game
        gui.keyDown('x')
        gui.keyUp('x')

    #change pyautogui delay back
    gui.PAUSE = 0.1