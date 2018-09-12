#!/usr/bin/python
"""
"""
import sys

class GameBoard(object): # all classes should be new-style
    """Handles the current and future states of a tic-tac-toe board.

    Encompasses GameState, some of get_user_move, generate_game_tree 
    and print_board.

    """
    def __init__(self, size):
        self.clear = "\n" * 100
        self.player_turn = None
        assert size >2 and < 9
        self.size = size
        self.moves = [' '] * size * size
        self.done = 0

    def __str__(self):
        # Clear the board
        result = self.clear
        # Print Player's Turn
        result += "Your turn (Player %s)" % (self.player_turn )
        # Print Board
        result += self.__print_board(self.moves)
        # Print Legend
        result += "\n Legend:\n"
        result +=  self.__print_board([ord(i) for i in range(65, 65 +(self.size *self.size))])
        return result

    def __print_board(self, positions):
        move_string = ''
        for _ in range(self.size):
            move_string += '|%s'*self.size
            move_string += '\n'
        return (move_string % positions)

    def get_user_move(self):
        while True:
            # Asks for move from player
            try:
                move = ord(input("Enter Move: ")) - 65
            # Turns Keyboard Interrupt into Game Exit
            except:
                sys.exit(0)
            # Check that move is on the game board
            if move < 0 or move > (self.size*self.size):
                print("Input is not a valid move. Please enter a move from the Legend.")
            # Check that the move has not already been played
            elif self.moves[self.move] != ' ':
                print("Move is already taken. Pick another move")
            else:
                break
        return move

    def play_move(self, move, player):
        self.moves[move] = player.symbol

    def generate_game_tree():
        pass

    def print_winner(self):
        if self.done ==0:
            print("But the game isn't over yet!")
        elif len(self.winners) == 1:
            print("The winner is player %s!" % (self.winners[0].symbol))
        else:
            print("It's a tie!")
            for winner in self.winners:
                print("Congratulations player %s!\n" % winner.symbol)



class Player(object):
    """Metaclass for the next two classes.

    All Players will have a symbol attribute and a make_move method 
    (which will just 'raise NotImplementedError' here).

    """
    def __init(self, symbol):
        self.symbol = symbol
    def make_move(self):
        raise NotImplementedError


class HumanPlayer(Player):
    """Handles all the user input stuff.

    Encompasses the rest of get_user_move.

    """
    pass


class ComputerPlayer(Player):
    """Handles AI stuff.

    Encompasses generate_best_move and minimax.

    """
    pass