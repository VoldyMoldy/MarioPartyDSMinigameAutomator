from tkinter import *
from tkinter.ttk import *
from get_the_lead_out import get_lead_out
from sweet_sleuth import sweet_sleuth

#hub window to access all scripts easily
hub_window = Tk()
hub_window.geometry('800x480')
hub_window.title('Mario Party DS Minigame Player')
hub_window.iconbitmap('images/hub/dice_block.ico')

# TODO
#create button for each minigame with a script to play it
#clicking the button should run the script after a configurable delay
#maybe also attempt to switch to desmume window on press idk
#complete story mode of the game to unlock all minigames (done, used a cheat code to unlock all minigames and modes)

#find games to automate (could check yt, but should play through them first)

#customizable delay before starting a script
delay = 5
delay_field = Text(hub_window, height = 5, width = 20)

#update delay
def update_delay():
    global delay
    delay = delay_field.get(index1 = 1)

delay_button = Button(hub_window, text = 'Update Delay', command = update_delay())

#sweet sleuth - use image recognition to find candies to bring to shy guy
sweet_button = Button(hub_window, text = 'Sweet Sleuth', bg = 'gray', command = sweet_sleuth(delay))

#get the lead out - button mash
lead_button = Button(hub_window, text = 'Get The Lead Out', bg = 'white', command = get_lead_out(delay))

mainloop()
