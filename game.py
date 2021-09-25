from ctypes import Array
from imagesProcessor import concat_tile_resize
from cv2 import hconcat, sampsonDistance, vconcat
import cv2
import numpy as np
from card import Card, Color, Filling, Shape


def isSet(card1: Card, card2: Card, card3: Card):
    ColorOk = False
    ShapeOk = False
    FillingOk = False
    CountOk = False

    # check matchings
    if ((card1.color != card2.color != card3.color and card1.color != card3.color) or 
    (card1.color == card2.color == card3.color and card1.color == card3.color)):
        ColorOk = True

    if ((card1.shape != card2.shape != card3.shape and card1.shape != card3.shape) or 
    (card1.shape == card2.shape == card3.shape and card1.shape == card3.shape)):
        ShapeOk = True
    
    if ((card1.filling != card2.filling != card3.filling and card1.filling != card3.filling) or 
    (card1.filling == card2.filling == card3.filling and card1.filling == card3.filling)):
        FillingOk = True
    
    if ((card1.count != card2.count != card3.count and card1.count != card3.count) or 
    (card1.filling == card2.count == card3.count and card1.count == card3.count)):
        CountOk = True
    
    return ColorOk and ShapeOk and FillingOk and CountOk

def showSet(card1: Card, card2: Card, card3: Card):
    picNum1 = str(card1.color) + str(card1.shape) + str(card1.filling) + str(card1.count)
    picNum2 = str(card2.color) + str(card2.shape) + str(card2.filling) + str(card2.count)
    picNum3 = str(card3.color) + str(card3.shape) + str(card3.filling) + str(card3.count)
    img1 = cv2.imread(f"./pics/{picNum1}.png",1)
    img2 = cv2.imread(f"./pics/{picNum2}.png",1)
    img3 = cv2.imread(f"./pics/{picNum3}.png",1)
    img1 = cv2.resize(img1, (0,0), None, 0.5, 0.5)
    img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)
    img3 = cv2.resize(img3, (0,0), None, 0.5, 0.5)
    img = concat_tile_resize([[img1,img2,img3]])
    cv2.imshow('Found this set!', img)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()

def searchSet (cards):
    for card1 in cards:
        for card2 in cards:
            for card3 in cards:
                if (card1 != card2 != card3 and card1 != card3):
                    if (isSet(card1, card2, card3)):
                        print('found Set!')
                        showSet(card1, card2, card3)
                        return # get out if found
