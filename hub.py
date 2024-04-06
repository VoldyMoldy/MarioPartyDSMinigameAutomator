#for all minigame scripts that require image detection the program assumes the emulator is fully on screen

#import libraries to create window
from tkinter import *
from tkinter.ttk import *

#import minigame scripts to be run on button click
from get_the_lead_out import get_lead_out
from goomba_wrangler import goomba_wrangler
from rail_riders import ride_rails

#functions to run minigame scripts
def run_get_lead_out():
    get_lead_out()

def run_goomba_wrangler():
    goomba_wrangler()

def run_rail_riders():
    ride_rails()  

#hub window to access all scripts easily
hub_window = Tk()
hub_window.geometry('350x50')
hub_window.title('Mario Party DS Minigame Player')
hub_window.iconbitmap('images/hub/dice_block.ico')

# TODO
#create button for each minigame with a script to play it
#clicking the button should run the script after a configurable delay
#complete story mode of the game to unlock all minigames (done, used a cheat code to unlock all minigames and modes)
#find games to automate (could check yt, but should play through them first)


#buttons to run minigames
btn_get_lead_out = Button(hub_window, text = "Get the Lead Out", command = run_get_lead_out)
btn_get_lead_out.grid(row = 0, column = 0, padx = 10, pady=10)

btn_goomba_wrnagler = Button(hub_window, text = "Goomba Wrangler", command = run_goomba_wrangler)
btn_goomba_wrnagler.grid(row = 0, column = 1, padx = 10, pady=10)

btn_rail_riders = Button(hub_window, text = "Rail Riders", command = run_rail_riders)
btn_rail_riders.grid(row = 0, column = 2, padx = 10, pady=10)

hub_window.mainloop()
