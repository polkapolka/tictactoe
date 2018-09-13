#!/usr/bin/python
"""
"""
import sys

class GameBoard(object): # all classes should be new-style
    """Handles the current and future states of a tic-tac-toe board.

    Encompasses GameState, some of get_user_move, generate_game_tree 
    and __print_board.

    """
    def __init__(self, size):
        self.clear = "\n" * 100
        self.player_turn = ' '
        assert size > 2 and size < 9
        self.size = size
        self.moves = [' '] * size * size
        self.done = 0

    def __str__(self):
        # Clear the board
        result = self.clear
        # Print Player's Turn
        result += "Your turn (Player %s)\n" % (self.player_turn )
        # Print Board
        result += self.__print_board(self.moves)
        # Print Legend
        result += "\n Legend:\n"
        result +=  self.__print_board([chr(i) for i in range(65, 65 +(self.size *self.size))])
        return result

    def __print_board(self, positions):
        move_string = ''
        for _ in range(self.size):
            move_string += '|%s'*self.size
            move_string += '\n'
        return (move_string % tuple(positions))

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
            elif self.moves[move] != ' ':
                print("Move is already taken. Pick another move")
            else:
                break
        return move

    def turn(self, move):
        self.moves[move] = self.player_turn
        if self.check_win():
            self.winners =[self.player_turn]
        elif self.check_tie():
            self.winners = [' ']
            self.done = -1

    def generate_game_tree(self, computer_player):
        pass

    def check_win(self):
        is_win =False
        locations = range(self.size * self.size)
        horizontals = [self.moves[i*self.size:(i+1)*self.size] for i in range(self.size)]
        verticals = [[self.moves[i+k*self.size] for k in range(self.size)] for i in range(self.size)]
        diagonals = [[self.moves[i*self.size+i] for i in range(self.size)],[self.moves[(i+1)*self.size -(i+1)] for i in range(self.size)]]
        for line in horizontals+verticals+diagonals:
            is_win = self.check_win_line(line)
            if is_win:
                self.done = 1
                break
        return is_win

    def check_win_line(self, line):
        if any([l==' 'for l in line]):
            return False
        elif all([line[0]==line[i] for i in range(self.size)]):
            return True
        else:
            return False

    def check_tie(self):
        if any([m==' ' for m in self.moves]):
            return False
        return True


    def print_winner(self):
        if self.done ==0:
            print("But the game isn't over yet!")
        elif self.done == 1:
            print("The winner is player %s!" % tuple(self.winners))
        elif self.done == -1:
            print("It's a tie!")



class Player(object):
    """Metaclass for the next two classes.

    All Players will have a symbol attribute and a make_move method 
    (which will just 'raise NotImplementedError' here).

    """
    def __init__(self, symbol):
        self.symbol = symbol
    def make_move(self):
        raise NotImplementedError


class HumanPlayer(Player):
    """Handles all the user input stuff.

    Encompasses the rest of get_user_move.

    """
    def make_move(self, game_board):
        return game_board.get_user_move()
        


class ComputerPlayer(Player):
    """Handles AI stuff.

    Encompasses generate_best_move and minimax.

    """
    def generate_best_move(self):
        pass
    def minimax(self):
        pass