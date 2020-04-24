class Player:
    def __init__(self, name, character):
        self.name = name
        # this is private attribute
        self.__character = character


player = Player(34, 45)
print player.name
