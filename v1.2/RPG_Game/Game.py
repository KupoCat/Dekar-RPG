import Util_Functions
from kivy.core.window import Keyboard, Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from player import Player
import kivy.clock
import keyboard
import obstacle

Util_Functions.os.environ['KIVY_IMAGE'] = 'pil,sdl2'


class RPG(FloatLayout, keyboard.MyKeyboardListener): # Graphics class for the Game
    def __init__(self, **kwargs):
        super(RPG, self).__init__(**kwargs)
        # Console size
        self.sizeX, self.sizeY = 800, 600
        # Background init
        self.background = Image(x=0, y=0, source=Util_Functions.path("\Background\Road01.png"))
        # Click counter init
        self.room_i, self.room_j = 1, 1
        self.counter = Label(color=(0, 0, 0, 5), font_size=28, x=300, y=250,
                             text=str(self.room_i) + '-' + str(self.room_j))
        # Player init
        self.player = Player(Util_Functions.path("\Players\Dekar_shit.png"), 0, 0)
        # Obstacles init
        self.obstacle_list = list()
        # Adding widgets
        self.add_widget(self.background)
        self.add_widget(self.player.image)
        self.add_widget(self.counter)
        self.update_map()

    def on_touch_down(self, touch):
        self.player.x, self.player.y = Util_Functions.touch_to_float_layout(touch, self.sizeX, self.sizeY)
        self.update_counter()

    def valid_room(self):
        return 1 <= self.room_i <= 4 and 1 <= self.room_j <= 4

    def create_obstacle(self, source, i, j):
        temp = obstacle.Obstacle(source=source, i=i, j=j)
        self.add_widget(temp.image)
        self.obstacle_list.append(temp)

    def update_counter(self):
        self.counter.text = text=str(self.room_i) + '-' + str(self.room_j)

    def update_map(self):
        for obs in self.obstacle_list:
            self.remove_widget(obs.image)
        self.obstacle_list = list()
        f = open(Util_Functions.path("\Data\Maps.txt"), "r")
        for line in f:
            if line[0] == str(self.room_i) and line[1] == str(self.room_j):
                self.create_obstacle(Util_Functions.path("\Obstacles\\" + line[5:]), int(line[2]), int(line[3]))



    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.player.move(self.obstacle_list, keycode[1]) is None:
            flag = self.check_pos(self.player)
            self.update_map()


    def check_pos(self, player):
        flag = True
        if player.image.x >= self.sizeX / 2:
            player.image.x -= self.sizeX
            player.j = 0
            self.room_j += 1
            if not self.valid_room():
                self.room_j -= 1
                player.move(self.obstacle_list, "left")
                player.j = 9
                player.image.x += self.sizeX
                flag = False
        elif player.image.x <= -self.sizeX / 2:
            player.image.x += self.sizeX
            player.j = 9
            self.room_j -= 1
            if not self.valid_room():
                self.room_j += 1
                player.move(self.obstacle_list, "right")
                player.j = 0
                player.image.x -= self.sizeX
                flag = False
        elif player.image.y >= self.sizeY / 2:
            player.image.y -= self.sizeY
            player.i = 0
            self.room_i += 1
            if not self.valid_room():
                self.room_i -= 1
                player.move(self.obstacle_list, "down")
                player.i = 9
                player.image.y += self.sizeY
                flag = False
        elif player.image.y <= -self.sizeY / 2:
            player.image.y += self.sizeY
            player.i = 9
            self.room_i -= 1
            if not self.valid_room():
                self.room_i += 1
                player.move(self.obstacle_list, "up")
                player.image.y -= self.sizeY
                player.i = 0
                flag = False
        else:
            flag = False
        self.update_counter()
        return flag


class RPGApp(App):  # Application class that creates a singleton of the RPG Game class
    def build(self):
        return RPG()

RPGApp().run()  # Run the application
