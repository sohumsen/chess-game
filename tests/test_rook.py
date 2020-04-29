from pieces import Rook
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_Rook(unittest.TestCase):
    def test_Rook1(self):
        board = Board()
        Board.populateBoard(board)
        b = Rook("ddd", Pos("h1"), board)
        self.assertEqual(b.move_piece(Pos("h5")), True)

        self.assertRaises(Exception, b.move_piece, Pos("a3"))


if __name__ == "__main__":
    unittest.main()
