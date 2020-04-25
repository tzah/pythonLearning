class Player:
    def __init__(self, name, sign):
        self.name = name
        # this is private attribute
        self.sign = sign

    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name
