#goomba wrangler has players circle goombas to score points and avoid circling bombs
import keyboard as key
import pyautogui as gui
import time
import pygetwindow as gw

def get_lead_out():
    #change pyautogui delay to mash faster
    gui.PAUSE = 0.001
    
    # switch to emulator
    window = gw.getWindowsWithTitle("DeSmuME")[0]
    window.activate()

    #get window position so program knows where to search
    left, top, width, height = window.left, window.top, window.width, window.height

    #only search the touch screen
    region_to_search = (left, top + height/2, width, height/2)

    #delay the program starting to not mash early and mess up any menuing or switching to game window
    time.sleep(3)

    start_time = time.time()
    while time.time() - start_time <= 20:
        #emergency escape key since it is bound to left shoulder, which is not used for any minigames
        if key.is_pressed('q'):
            exit(0)

    #change pyautogui delay back
    gui.PAUSE = 0.1