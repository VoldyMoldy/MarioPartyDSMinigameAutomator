#goomba wrangler has players circle goombas to score points and avoid circling bombs
import keyboard as key
import pyautogui as gui
import time
import pygetwindow as gw

def draw_circle(x: int, y: int):
    #function to draw circle around the coords of a found goomba
    #draws a hexagon instead because the game still counts it and is easier to code
    gui.moveTo(x + 20, y)
    gui.mouseDown()
    gui.moveTo(x + 15, y + 15)
    gui.moveTo(x, y + 20)
    gui.moveTo(x - 15, y + 15)
    gui.moveTo(x - 20, y)
    gui.moveTo(x - 15, y - 15)
    gui.moveTo(x, y - 20)
    gui.moveTo(x + 15, y - 15)
    gui.moveTo(x + 20, y)
    gui.mouseUp()

def goomba_wrangler():
    #change pyautogui delay to circle faster
    gui.PAUSE = 0.01
    
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
        #try locating either a golden goomba (+3) or normal goomba (+1), return none if not found
        try:
            gold = gui.locateOnScreen('images/goomba_wrangler/gold.png', region = region_to_search)
        
        except ImageNotFoundException as e:
            gold = None
            
            try: #only try and find normal goombas if no golden goombas are found
                normal = gui.locateOnScreen('images/goomba_wrangler/goomba.png', region = region_to_search)
            except ImageNotFoundException as e:
                normal = None
        if gold != None: #check if there is a gold goomba first, if so prioritize circling it first
            draw_circle(gold)
        elif normal != None: #check if there are any avaliable goombas to circle
            draw_circle(normal)

    #change pyautogui delay back
    gui.PAUSE = 0.1