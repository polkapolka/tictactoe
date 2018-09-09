#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A classic tic-tac-toe game programmed for
the command line.

"""

import random

class Board():
	def __init__(self):
		self. spaces = [None] * 9
		self.win = False
		self.tie = False
	def __str__(self):
		return '               Y\n          1    2    3    \n      1:  %s | %s | %s \n X    2:  %s | %s | %s \n      3:  %s | %s | %s ' % tuple([s if s else ' ' for s in self.spaces])
	def move(self, player, x, y):
		loc = 3*(int(x)) +int(y)
		self.spaces[loc] = player
		self.__check_win(player)
	def __check_win_row(self, a_player,a_list):
		return all([x==a_player for x in a_list])
	def __check_win(self, player):
		if self.__check_win_row(player,self.spaces[0:3]) \
		or self.__check_win_row(player,self.spaces[3:6]) \
		or self.__check_win_row(player,self.spaces[6:9]):
			self.win = True
		elif self.__check_win_row(player, [self.spaces[i] for i in [0,3,6]]) \
		or self.__check_win_row(player, [self.spaces[i] for i in [1,4,7]]) \
		or self.__check_win_row(player, [self.spaces[i] for i in [2,5,8]]):
			self.win = True
		elif self.__check_win_row(player, [self.spaces[i] for i in [0,4,8]]) \
		or self.__check_win_row(player, [self.spaces[i] for i in [2,4,6]]):
			self.win = True
		elif not any([x==None for x in self.spaces]):
			self.tie = True
	def oponent_move(self, player):
		move = random.choice([i for i in range(9) if self.spaces[i]==None])
		self.spaces[move] = player
		self.__check_win(player)



def PrintHeader():
	result = '\n'
	result += '\tTic-Tac-Toe Game\t\n\n'
	print(result)

def GetResponse():
	play = [None, None]
	print("How do you want to move? ")
	play[0] = int(input("X: "))-1
	play[1] = int(input("Y: "))-1
	return play

def SwapPlayer(player):
	if player =='X':
		return 'O'
	elif player == 'O':
		return 'X'
	else:
		raise ValueError

def PrintWinner(player):
	result = '\n'
	result += 'And the Winner is ....\n'
	result += 'Player %s has WON THE GAME!!!' % (player)
	print(result)

def PrintTie():
	result = '\n'
	result += 'Womp, Womp ....\n'
	result += "It's a Tie!!!" 
	print(result)

def main():
	playing = True
	new_game = Board()
	player = 'X'
	while playing:
		PrintHeader()
		print(new_game)
		play = GetResponse()
		new_game.move(player, play[0], play[1])
		if new_game.win or new_game.tie:
			break
		player = SwapPlayer(player)
		new_game.oponent_move(player)
		player = SwapPlayer(player)
		
	if new_game.win:
		PrintWinner(player)
	else:
		PrintTie()

if __name__=='__main__':
	main()