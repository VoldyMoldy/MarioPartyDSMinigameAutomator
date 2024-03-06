#rail riders has the players swipe up on the touch screen as fast as possible to go down a railing quickly and make the biggest jump
import keyboard as key
import pyautogui as gui
import time
import pygetwindow as gw

def ride_rails():
    #change pyautogui delay to swipe the touch screen faster
    gui.PAUSE = 0.01
    
    # switch to emulator
    window = gw.getWindowsWithTitle("DeSmuME")[0]
    window.activate()

    #get window position so program knows where to swipe
    left, top, width, height = window.left, window.top, window.width, window.height

    startDrag = (left + width/2, top + height*(7/8))
    endDrag = (left + width/2, top + height*(5/8))

    #delay the program starting to not swipe early and mess up any menuing or switching to game window
    time.sleep(2)

    start_time = time.time()
    while time.time() - start_time <= 15:
        #emergency escape key since it is bound to left shoulder, which is not used for any minigames
        if key.is_pressed('q'):
            exit(0)
        #swipe fast enough to probably destroy a physical touch screen
        gui.moveTo(startDrag) #about the bottom middle of the touch screen
        gui.mouseDown()
        gui.moveTo(endDrag, duration = 0.02) #move to the top middle of the touch screen 5 times per second
        gui.mouseUp()

    #change pyautogui delay back
    gui.PAUSE = 0.1