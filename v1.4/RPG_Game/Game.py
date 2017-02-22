import Util_Functions
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from player import Player
import kivy.clock
import keyboard
import obstacle
import npc
Util_Functions.os.environ['KIVY_IMAGE'] = 'pil,sdl2'


class RPG(FloatLayout, keyboard.MyKeyboardListener): # Graphics class for the Game
    def __init__(self, **kwargs):
        super(RPG, self).__init__(**kwargs)
        # Get name
        # self.name = name
        # Console size
        self.sizeX, self.sizeY = 800, 600
        # Background init
        self.background = Image(x=0, y=0, source=Util_Functions.path("\Background\Road01.png"))
        # Click counter init
        self.room_i, self.room_j = 1, 1
        self.counter = Label(color=(0, 0, 0, 5), font_size=28, x=300, y=250,
                             text=str(self.room_i) + '-' + str(self.room_j))
        # Player init
        self.player = Player(Util_Functions.path("\Players\Dekar_shit.png"), 1, 0)
        # Obstacles init
        self.obstacle_list = list()
        # NPC init
        self.npc_list = list()
        # Items init
        self.items = dict()
        # Adding widgets
        self.add_widget(self.background)
        self.add_widget(self.player.image)
        self.add_widget(self.counter)
        self.update_map()


    def on_touch_down(self, touch):
        x, y = Util_Functions.touch_to_float_layout(touch)
        i, j = Util_Functions.location_to_cords(x, y)
        i, j = int(i), int(j)
        print i, j
        f = open(Util_Functions.path("Data\\" + str(self.room_i) + '-' + str(self.room_j)+ ".txt"), 'a')
        f.write(str(self.room_i) + str(self.room_j) + str(i) + str(j) + str(1) + " Rock.png\n")
        self.update_map()
        # print self.name


    def valid_room(self):
        return 1 <= self.room_i <= 4 and 1 <= self.room_j <= 4

    def create_obstacle(self, source, i, j):
        temp = obstacle.Obstacle(source=source, i=i, j=j)
        self.add_widget(temp.image)
        self.obstacle_list.append(temp)

    def create_npc(self, source, i, j, text, quest_details, quest_amount):
        temp = npc.Npc(source=source, i=i, j=j, text=text, quest_details=quest_details, quest_amount=quest_amount)
        self.add_widget(temp.image)
        self.npc_list.append(temp)

    def update_counter(self):
        self.counter.text = text=str(self.room_i) + '-' + str(self.room_j)

    def update_map(self):
        for obs in self.obstacle_list:
            self.remove_widget(obs.image)
        self.obstacle_list = list()

        for npc in self.npc_list:
            self.remove_widget(npc.image)
        self.npc_list = list()

        f = open(Util_Functions.path("Data\\" + str(self.room_i) + '-' + str(self.room_j)+ ".txt"), "r")
        for line in f:
            if line[0] == str(self.room_i) and line[1] == str(self.room_j):
                if line[4] == str(1):
                    self.create_obstacle(Util_Functions.path("\Obstacles\\" + line[6:len(line)-1]), int(line[2]), int(line[3]))
                elif line[4] == str(2):
                    i1, j1 = line[2], line[3]
                    line = line[6:]
                    start, end, source, text = 0, 0, 0, 0
                    for i, j in enumerate(line):
                        if j == ' ':
                            start = i
                            break
                    source = line[:start]
                    line = line[start+2:]
                    for i, j in enumerate(line):
                        if j == "\"":
                            end = i
                            break
                    line = line[end+2:]
                    quest_details = line[:end]
                    index1 = end
                    for i, j in enumerate(line):
                        if j == "\"":
                            index1 = i
                            break
                    quest_details = line[:index1]
                    line = line[index1:]
                    for i, j in enumerate(line):
                        if j == "\"":
                            start = i
                            break
                    quest_amount = line[:start]
                    text = line[start+1:len(line)-1]
                    if quest_details not in self.items.keys():
                        self.items[quest_details] = [0, quest_amount]
                    self.create_npc(Util_Functions.path("\Obstacles\\" + source), int(i1), int(j1), text=text, quest_details=quest_details, quest_amount=line[end+2:])

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'i':
            self.display_inventory()
        elif keycode[1] == 'q':
            self.display_quests()
        elif keycode[1] == 'm':
            self.display_map()
        flag = self.player.move(self.obstacle_list + self.npc_list, keycode[1])
        if flag is True:
            flag2 = self.check_pos(self.player)
            if flag2 is True:
                self.update_map()
        elif flag is None:
            self.player.interaction(self.npc_list, keycode[1])

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
            flag = None
        self.update_counter()
        return flag

class StartScreen(FloatLayout, keyboard.MyKeyboardListener):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.title = Label(x=0, y=250, font_size = 48, text="Please enter your name (just type)\n tap caps/shift for caps")
        self.add_widget(self.title)
        self.name = str()
        self.presented_name = Label(x=-250, y=150, name=self.name, font_size = 32, color=(1,0,0,1))
        self.add_widget(self.presented_name)
        self.caps = False
        self.start = Label(color=(1,1,0,1), x=0, y=-300, text='START GAME')

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'shift' or keycode[1] == 'capslock':
            self.caps = not self.caps
        elif Util_Functions.isABC(keycode[1]):
            if self.caps is False:
                self.name += keycode[1]
            else:
                self.name += chr(ord(keycode[1]) + ord('A') - ord('a'))
        elif keycode[1] == 'spacebar':
            self.name += ' '
        elif keycode[1] == 'backspace':
            self.name = self.name[:len(self.name)-1]
        self.update_name()

    def on_touch_down(self, touch):
        if self.start.x + 100 > touch.x + 400 > self.start.x:
            self.stop()

    def update_name(self):
        self.presented_name.text = self.name
        self.remove_widget(self.presented_name)
        self.add_widget(self.presented_name)


class RPGApp(App):  # Application class that creates a singleton of the RPG Game class
    def build(self):
        return RPG()


class StartApp(App):
    def build(self):
        return StartScreen()

    def on_stop(self):
        self.game.run()

RPGApp().run()
