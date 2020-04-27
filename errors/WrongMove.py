class WrongMove(Exception):
    def __init__(self, row, col):
        if row > 2 or row < 0:
            self.value = "row error! must be between 0 - 2"
        if col > 2 or row < 0:
            self.value = "col error! must be between 0 - 2"

    def get_value(self):
        return self.value
