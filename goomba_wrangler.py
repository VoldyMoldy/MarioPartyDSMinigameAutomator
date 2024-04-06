#goomba wrangler has players circle goombas to score points and avoid circling bombs
import keyboard as key
import pyautogui as gui
import time
import pygetwindow as gw
import math

#TODO: maybe make the program watch out for bombs, otherwise wins a good majority of the time

def draw_circle(x: int, y: int, radius: int = 40, num_points: int = 30):
    #smoothly draw a circle around the given coordinates
    angle_increment = 2 * math.pi / num_points

    gui.moveTo(x + radius, y, 0.05)
    gui.mouseDown()

    for i in range(num_points + 5): #have some point overlap to ensure closed circle
        angle = i * angle_increment
        next_x = x + radius * math.cos(angle)
        next_y = y + radius * math.sin(angle)
        gui.moveTo(next_x, next_y, 0.05)

    gui.mouseUp()

def goomba_wrangler():
    #change pyautogui delay to circle faster
    gui.PAUSE = 0.0075
    
    # switch to emulator
    window = gw.getWindowsWithTitle("DeSmuME")[0]
    window.activate()

    #get window position so program knows where to search
    left, top, width, height = window.left, window.top, window.width, window.height

    #only search the touch screen
    region_to_search = (left, top + height//2, width, height//2)

    #delay the program starting to not mess up any menuing or waste minigame time
    time.sleep(1)

    start_time = time.time()
    while time.time() - start_time <= 23:
        #emergency escape key since it is bound to left shoulder, which is not used for any minigames
        if key.is_pressed('q'):
            exit(0)
        #try locating either a golden goomba (+3) or normal goomba (+1), return none if not found
        gold = None
        gold = gui.locateCenterOnScreen('images/goomba_wrangler/gold.png', region = region_to_search, confidence = 0.60)
        normal = None
        normal = gui.locateCenterOnScreen('images/goomba_wrangler/goomba.png', region = region_to_search, confidence = 0.60)
        
        if gold is not None: #check if there is a gold goomba first, if so prioritize circling it first
            draw_circle(*gold)
        elif normal is not None: #check if there are any avaliable goombas to circle
            draw_circle(*normal)
        #else just move on and search again

    #change pyautogui delay back
    gui.PAUSE = 0.1