import Util_Functions
from kivy.uix.label import Label

class Npc():
    def __init__(self, source, i, j, text, quest_details, quest_amount):
        x, y = Util_Functions.cords_to_location(i, j)
        self.image = Util_Functions.Image(source=source, x=x, y=y)
        self.i = i
        self.j = j
        self.text = Label(text=text)
        self.quest = (quest_details, quest_amount)

