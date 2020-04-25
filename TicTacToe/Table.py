import sys
import errors


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
            print("")

    def player_move(self, player):
        move_flag = True
        while move_flag:
            try:
                row = int(raw_input(player.get_name() + " its your turn please insert row: "))
                col = int(raw_input(player.get_name() + " its your turn please insert col: "))
                if row > 2 or col > 2 or col < 0 or row < 0:
                    raise errors.WrongMove(row, col)
                if self.table[row][col][0] == '_':
                    move_flag = False
                    self.table[row][col][0] = player.get_sign()
                    self.counter = self.counter - 1
                self.print_table()
                if self.winner(player):
                    print "%s you win", player.get_name()
                    sys.exit(player.get_name() + " is the winner")
            except errors.WrongMove as e:
                print e.get_value()

    # mean that we can assign the player sign

    def is_finish(self):
        if self.counter == 0:
            return True
        return False

    def winner(self, player):
        counter_row = 0
        counter_col = 0
        counter_x = 0
        # check the rows
        for i in range(3):
            for j in range(3):
                if self.table[j][i][0] == player.sign:
                    counter_col = counter_col + 1
                if self.table[i][j][0] == player.sign:
                    counter_row = counter_row + 1
                if i == j:
                    if self.table[i][j][0] == player.sign:
                        counter_x = counter_x + 1
            if counter_row == 3 or counter_col == 3:
                return True
            counter_col = 0
            counter_row = 0
        if counter_x == 3:
            return True
        return False
