import Util_Functions


class Player:
    def __init__(self, source, spawnX, spawnY):
        x, y = Util_Functions.cords_to_location(spawnX, spawnY)
        self.image = Util_Functions.Image(source=source, x=x, y=y)
        self.j = spawnX
        self.i = spawnY

    def in_range(self, other):
        if other.j == self.j:
            if other.i + 1 == self.i or other.i - 1 == self.i:
                return True
        elif other.i == self.i:
            if other.j + 1 == self.j or other.j - 1 == self.j:
                return True

    def interaction(self, npc_list, key):
        if key == 'spacebar':
            print len(npc_list)
            for npc in npc_list:
                if self.in_range(npc):
                    print npc.text.text

    def move(self, obstacle_list, direction):
        if direction == "left":
            for obs in obstacle_list:
                if obs.j == self.j - 1 and obs.i == self.i:
                    return False
            self.image.x -= 80
            self.j -= 1
            return True
        elif direction == "right":
            for obs in obstacle_list:
                if obs.j == self.j + 1 and obs.i == self.i:
                    return False
            self.image.x += 80
            self.j += 1
            return True
        elif direction == "up":
            for obs in obstacle_list:
                if obs.j == self.j and obs.i - 1 == self.i:
                    return False
            self.image.y += 60
            self.i += 1
            return True
        elif direction == "down":
            for obs in obstacle_list:
                if obs.j == self.j and obs.i + 1 == self.i:
                    return False
            self.image.y -= 60
            self.i -= 1
            return True
        else:
            return None
