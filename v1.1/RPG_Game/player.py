import Util_Functions


class Player:
    def __init__(self, source, spawnX, spawnY):
        x, y = Util_Functions.cords_to_location(spawnX, spawnY)
        self.image = Util_Functions.Image(source=source, x=x, y=y)
        self.i = spawnX
        self.j = spawnY

    def move(self, direction):
        if direction == "left":
            self.image.x -= 80
            self.i -= 1
        elif direction == "right":
            self.image.x += 80
            self.i += 1
        elif direction == "up":
            self.image.y += 60
            self.j += 1
        elif direction == "down":
            self.image.y -= 60
            self.j -= 1
        else:
            return 0
