#!/usr/bin/python
"""
unittest for testing utils.py  
"""

import utils
import unittest
from unittest.mock import patch
import sys

class PlayerTest(unittest.TestCase):
	def setUp(self):
		self.test_player = utils.Player('X')
	def testMakeMove(self):
		self.assertRaises(NotImplementedError, self.test_player.make_move)


class HumanPlayerTest(unittest.TestCase):
	def setUp(self):
		self.test_human_player = utils.HumanPlayer('X')
		self.test_game_board = utils.GameBoard(3)

	def testMakeMove(self):
		input_data = 'A'
		expected = ord('A')-65
		utils.input = lambda _: input_data
		actual = self.test_human_player.make_move(self.test_game_board)
		self.assertEqual(actual, expected)



def main():
	unittest.main()

if __name__ == '__main__':
    main()


"""
[tictactoe] python3 test.py                                                                                                                                                              21:41:20  ☁  master ☂ ⚡ ✭
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
"""