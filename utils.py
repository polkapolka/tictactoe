#!/usr/bin/python
"""
Contains Classes called by tictactoe.py.  
"""
import sys

class GameBoard(object): # all classes should be new-style
    """Handles the current and future states of a tic-tac-toe board.

    Has-A GameState, some of get_user_move, calls generate_game_tree 
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

    def check_valid_move(self, move):
        # Check that move is on the game board
        if move < 0 or move > (self.size*self.size):
            print("Input is not a valid move. Please enter a move from the Legend.")
            move = None
        # Check that the move has not already been played
        elif self.moves[move] != ' ':
            print("Move is already taken. Pick another move")
            move = None
        return move

    def turn(self, move):
        self.moves[move] = self.player_turn
        if self.check_win(self):
            self.winners =[self.player_turn]
        elif self.check_tie():
            self.winners = [' ']
            self.done = -1

    @staticmethod
    def check_win(game_board):
        is_win =False
        locations = range(game_board.size * game_board.size)
        horizontals = [game_board.moves[i*game_board.size:(i+1)*game_board.size] for i in range(game_board.size)]
        verticals = [[game_board.moves[i+k*game_board.size] for k in range(game_board.size)] for i in range(game_board.size)]
        diagonals = [[game_board.moves[i*game_board.size+i] for i in range(game_board.size)],[game_board.moves[(i+1)*game_board.size -(i+1)] for i in range(game_board.size)]]
        for line in horizontals+verticals+diagonals:
            is_win = game_board.check_win_line(line)
            if is_win:
                game_board.done = 1
                break
        return is_win

    @staticmethod
    def check_win_line(line):
        if any([l==' 'for l in line]):
            return False
        elif all([line[0]==line[i] for i in range(len(line))]):
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

class GameState:
    """Creates a GameState Tree.

    Facilitates Minimax Algorithm for computer player.
    """
    def __init__(self, game_board):
        self.game_board = game_board
        self.children = []
        self.game_end = False

    def generate_children(self, player):
        open_moves = [i for i, x in enumerate(self.game_board) if x == ' ']

        for move in moves:
            child = GameState(self.game_board)
            child.game_board[move] = player
            child.set_winner()

        if child.game_end == False:
            child.generate_children('X' if player == 'O' else 'O')
            self.children.append(child)
        else:
            self.children.append(child)

    def set_winner(self):
        #X is given a positive score, O is given a negative score
        winner = self.game_board.check_win(game_board)
        if winner == 'X':
            self.score = 1
            self.game_end = True
        elif winner == 'O':
            self.score = -1
            self.game_end = True
        elif winner == -1:
            self.score = 0
            self.game_end = True
        else:
            self.score = 0
            self.game_end = False

    def check_win(self):
        pass



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
        while True:
            # Asks for move from player
            try:
                move = ord(input("Enter Move: ")) - 65
            # Turns Keyboard Interrupt into Game Exit
            except:
                sys.exit(0)
            if game_board.check_valid_move(move) is not None:
                break
        return move
        


class ComputerPlayer(Player):
    """Handles AI stuff.

    Encompasses generate_best_move and minimax.

    """
    def make_move(self, game_board):
        pass
    def generate_best_move(self):
        pass
    def minimax(self):
        pass