from pieces import Knight
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_King(unittest.TestCase):
    def test_knight(self):
        board = Board()
        Board.populateBoard(board)

        b = Knight("ddd", Pos("b1"), board)
        board.update(b)

        print("####################################")
        print(b.move_piece(Pos("d2")))


if __name__ == "__main__":
    unittest.main()
