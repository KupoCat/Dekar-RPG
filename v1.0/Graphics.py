import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from kivy.core.window import Keyboard, Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import kivy.clock

def touchToFloatLayeout(touch, sizex, sizey):
    des_x, des_y = touch.x - sizex/2, touch.y - sizey/2
    return (des_x, des_y)


def path(dir_path):
    real_path = os.path.dirname(os.path.realpath(__file__)) + dir_path
    return real_path


class MyKeyboardListener(Widget):
    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self, 'text')
        if self.keyboard.widget:
            pass
        self.keyboard.bind(on_key_down=self.on_keyboard_down)
        self.last_input = ''

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard = self.last_input

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.last_input = keycode[1]
        keyboard.release()


class RPG(FloatLayout): # Graphics class for the Game
    def __init__(self, **kwargs):
        super(RPG, self).__init__(**kwargs)
        self.sizeX = 800
        self.sizeY = 600
        self.background = Image(x=0, y=0, source=path("\grass.png"))
        self.add_widget(self.background)
        self.player = Image(x=-40, y=-30, source=path("\dekar_shit.png"))
        self.add_widget(self.player)
        self.click_counter = 0
        self.keyboard = MyKeyboardListener()
        self.counter = Label(color=(0,0,0,1), font_size=20, x=300, y=250, text = "Click counter : " + str(self.click_counter))
        self.add_widget(self.counter)
        self.last_input = str()
        kivy.clock.Clock.schedule_interval(self.check_input, 0.01)

    def on_touch_down(self, touch):
        self.player.x, self.player.y = touchToFloatLayeout(touch, self.sizeX, self.sizeY)
        self.update_counter()

    def update_counter(self):
        self.click_counter += 1
        self.counter.text = "Click counter : " + str(self.click_counter)

    def check_input(self, dt):
        if type(self.keyboard.keyboard) != Keyboard:
            self.last_input = self.keyboard.keyboard
            self.keyboard = MyKeyboardListener()
        else:
            if self.last_input == "left":
                self.player.x -= 80
                self.last_input = ''
            elif self.last_input == "right":
                self.player.x += 80
                self.last_input = ''
            elif self.last_input == "up":
                self.player.y += 60
                self.last_input = ''
            elif self.last_input == "down":
                self.player.y -= 60
                self.last_input = ''


class RPG_App(App): # Application class that creates a singleton of the RPG Game class
    def build(self):
        return RPG()

RPG_App().run() # Run the application

