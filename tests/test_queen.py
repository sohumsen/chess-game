from pieces import Queen
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_Queen(unittest.TestCase):
    def test_Queen(self):
        board = Board()
        Board.populateBoard(board)
        b = Queen("ddd", Pos("f1"), board)

        self.assertEqual(b.move_piece(Pos("h1")), True)
        b = Queen("ddd", Pos("f1"), board)
        self.assertRaises(InvalidMoveException, b.move_piece, Pos("h2"))


if __name__ == "__main__":
    unittest.main()
