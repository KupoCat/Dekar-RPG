import Util_Functions


class Obstacle:
    def __init__(self, source, i, j):
        x, y = Util_Functions.cords_to_location(i, j)
        self.image = Util_Functions.Image(source=source, x=x, y=y)
        self.i = i
        self.j = j
