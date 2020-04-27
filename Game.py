from TicTacToe import *

player1 = Player(raw_input("Player 1 please insert your name: "), 'X')
player2 = Player(raw_input("Player 2 please insert your name: "), 'O')
table = Table(player1, player2)
while not table.is_finish():
    table.player_move(player2)
    table.player_move(player1)
