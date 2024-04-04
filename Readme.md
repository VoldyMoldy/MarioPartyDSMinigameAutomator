# Mario Party DS Minigame Automator
A collection of python scripts to automate playing certain minigames from Mario Party DS.

## Setup
1. Download [DeSmuME](http://desmume.org/), as this will be the emulator used for playing the game.
2. Obtain a *legal* ROM of Mario Party DS, most likely by dumping the contents of your cartridge of the game. A copy of the rom will not be provided here.
3. Download this repository, and ensure that you have at least Python 3.11 installed, as well as the following libraries to make sure the scripts function properly.

   - pyautogui
   - tkinter
   - opencv-python
   - pygetwindow

## Use

1. Open DeSmuME and ensure that View > Window Size is set to 1 and View > Magnification Filter is set to 'Nearest 2X'. This is to ensure the image recognition in the scripts works properly.
2. Open your rom of Mario Party DS and enter the minigame mode.
3. Through the minigame mode menu, enter free play and set up a two player match.
4. Start any of the supported minigames and then click the corresponding button in the program window to start the script.
