import array as arr


class Table:
    def __init__(self, player1, player2):
        self.table = arr.array([], [])
        self.p1 = player1
        self.p2 = player2
