from pieces import King
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException

# The code to test
import unittest  # The test framework


class Test_King(unittest.TestCase):
    def test_King(self):
        board = Board()
        Board.populateBoard(board)
        b = King("ddd", algebra_to_cartesian("g1"), board)


if __name__ == "__main__":
    unittest.main()
