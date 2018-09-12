#!/usr/bin/python
"""
"""

from utils import ComputerPlayer, GameBoard, HumanPlayer
import sys

def create_player(symbol):
    """Takes user input on player type and returns a Player."""
    while True:
    	try:
		    player_type = input("Is player %s human or AI?\nEnter \'H\' for human, \'A\' for AI: " % symbol)
		except:
			sys.exit(0)
	    if player_type == 'H':
	    	return HumanPlayer(symbol)
	    elif player_type == 'A':
	    	return ComputerPlayer(symbol)
	    else:
	    	print("Invalid Entry.")

def pick_player(symbols):
    """Allow user to choose one of the symbols."""
    while True:
	    print("Who should go first?\n")
	    r_string = "Enter " +', '.join(["'%s' for player %s" % symbol for symbol in symbols]) + ":  "
	    try:
		    first_turn = input(r_string)
		except:
			sys.exit(0)
	    if first_turn in symbols:
		    break
		else:
			print("Invalid Entry.\n")
	return first_turn


def play_game(game_board, players):
    """Contains the main game loop."""
    while True:
    	pass
    print(game_board)
    game_board.print_winner()

def main():
    """Overall control of the game.

    Create two Players  with symbols 'X' and 'O' and a GameBoard, 
    pick_player for first and play_game.

    """
    SYMBOLS = ['X','O']
    game_board = GameBoard(3) # Creates a 3X3 game board
    players = {symbol:'' for symbol in SYMBOLS}
    for symbol in SYMBOLS:
	    players[symbol] = create_player(symbol)
    game_board.player_turn = pick_player(SYMBOLS)
    play_game(game_board, players)

if __name__ == '__main__':
    main()