from game import searchSet
from card import Card
from PIL.ImageOps import grayscale
import pyautogui
import os.path
import time

# checks the pic number contains only 1/2/3 chars
def validSequance(picNum):
    for char in list(picNum):
        if ((char != '1') and (char != '2') and (char != '3')):
            return False
    return True

time.sleep(2) # put page on your screen first
cards = []

# we need to get all pictures from pics
for picNum in range(1111, 3334):
    picNum = str(picNum)
    # check for:: 1) valid pic number  2) pic exists  3) pic found on screen
    if (validSequance(picNum) and os.path.exists(f"./pics/{picNum}.png") and pyautogui.locateOnScreen(f"./pics/{picNum}.png")):
        cards.append(Card(picNum[0], picNum[1], picNum[2], picNum[3]))  

if (len(cards) > 2):
    searchSet(cards)
else:
    print('i cant see enough cards... try again')
