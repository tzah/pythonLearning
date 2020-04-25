class WrongMove(Exception):
    def __init__(self, row, col):
        if row > 3 or row < 0:
            self.value = "row error! must be between 0 - 3"
        if col > 3 or row < 0:
            self.value = "col error! must be between 0 - 3"

    def get_value(self):
        return self.value
