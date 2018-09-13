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
        r_string = '\n'.join(["'%s' for player %s" % (symbol, symbol) for symbol in symbols]) + "\nEnter:  "
        try:
            first_turn = input(r_string)
        except:
            sys.exit(0)
        if first_turn in symbols:
            break
        else:
            print("Invalid Entry.\n")
    return first_turn

def set_order_of_play(symbols, no_turns=0):
    while True:
        if no_turns ==0:
            first_turn = pick_player(symbols)
            order_list = symbols[symbols.index(first_turn):] + symbols[:symbols.index(first_turn)]
        no_turns +=1
        current_turn = order_list.pop(0)
        order_list.append(current_turn)
        yield current_turn


def play_game(game_board, players, order_of_play):
    """Contains the main game loop."""
    while True:
        game_board.player_turn = next(order_of_play)
        print(game_board)
        move = players[game_board.player_turn].make_move(game_board)
        game_board.turn(move)
        if game_board.done != 0:
            break
    print(game_board)
    game_board.print_winner()

def main():
    """Overall control of the game.

    Create two Players  with symbols 'X' and 'O' and a GameBoard, 
    pick_player for first and play_game.

    """
    SYMBOLS = ['X','O']
    game_board = GameBoard(3)     # Creates a 3X3 game board
    players = {symbol:'' for symbol in SYMBOLS}
    for symbol in SYMBOLS:
        players[symbol] = create_player(symbol)
    order_of_play = set_order_of_play(SYMBOLS)
    play_game(game_board, players, order_of_play)

if __name__ == '__main__':
    main()
