from Table import Table
from Player import Player

player1 = Player(raw_input("Player 1 please insert your name: "), 'X')
player2 = Player(raw_input("Player 2 please insert your name: "), 'O')
table = Table(player1, player2)
while not table.is_finish():
    table.player_move(player2, int(raw_input("Player 2 its your turn please insert row: ")),
                      int(raw_input("Player 2 its your turn please insert col: ")))
    table.player_move(player1, int(raw_input("Player 1 its your turn please insert row: ")),
                      int(raw_input("Player 1 its your turn please insert col: ")))

