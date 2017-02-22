import os
from kivy.uix.image import Image


def touch_to_float_layout(touch):
    des_x, des_y = touch.x - 400, touch.y - 300
    return des_x, des_y


def isABC(key_code):
    if len(key_code) == 1 and 'a' <= key_code <= 'z':
        return True


def path(dir_path):
    real_path = os.path.dirname(os.path.realpath(__file__)) + "\Game Dependencies\\" + dir_path
    return real_path


def location_to_cords(x, y):
    temp_x = x+400
    temp_y = y+300
    return temp_y/60, temp_x/80


def cords_to_location(i, j):
    return -800/2 + j*80 +40, -600/2 + i*60 + 30
