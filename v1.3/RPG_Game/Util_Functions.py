import os
from kivy.uix.image import Image

def touch_to_float_layout(touch, sizeX, sizeY):
    des_x, des_y = touch.x - sizeX/2, touch.y - sizeY/2
    return des_x, des_y


def isABC(keycode):
    if len(keycode) == 1 and 'a' <= keycode <= 'z':
        return True


def path(dir_path):
    real_path = os.path.dirname(os.path.realpath(__file__)) + dir_path
    return real_path


def location_to_cords(x, y):
    temp_x = x+400
    temp_y = y+300
    return temp_x/80, temp_y/60


def cords_to_location(i, j):
    return -800/2 + j*80 +40, -600/2 + i*60 + 30
