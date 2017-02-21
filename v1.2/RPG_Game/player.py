import Util_Functions


class Player:
    def __init__(self, source, spawnX, spawnY):
        x, y = Util_Functions.cords_to_location(spawnX, spawnY)
        self.image = Util_Functions.Image(source=source, x=x, y=y)
        self.j = spawnX
        self.i = spawnY

    def move(self, obstacle_list, direction):
        if direction == "left":
            for obs in obstacle_list:
                if obs.j == self.j - 1 and obs.i == self.i:
                    return False
            self.image.x -= 80
            self.j -= 1
        elif direction == "right":
            for obs in obstacle_list:
                if obs.j == self.j + 1 and obs.i == self.i:
                    return False
            self.image.x += 80
            self.j += 1
        elif direction == "up":
            for obs in obstacle_list:
                if obs.j == self.j and obs.i - 1 == self.i:
                    return False
            self.image.y += 60
            self.i += 1
        elif direction == "down":
            for obs in obstacle_list:
                if obs.j == self.j and obs.i + 1 == self.i:
                    return False
            self.image.y -= 60
            self.i -= 1
        else:
            return None
