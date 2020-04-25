class Table:
    table = [[['_'], ['_'], ['_']], [['_'], ['_'], ['_']], [['_'], ['_'], ['_']]]
    counter = 9

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def print_table(self):
        for i in range(3):
            print("")
            for j in range(3):
                print(self.table[i][j][0]),
        print 'finish printing'

    def player_move(self, player, row, col):
        if self.table[row][col][0] == '_':
            self.table[row][col][0] = player.get_sign()
            self.counter = self.counter - 1
        self.print_table()

    # mean that we can assign the player sign

    def is_finish(self):
        if self.counter == 0:
            return True
        return False
