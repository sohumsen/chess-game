from pieces import Knight
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_Knight(unittest.TestCase):
    def test_Knight1(self):
        board = Board()
        Board.populateBoard(board)
        b = Knight("ddd", Pos("b1"), board)

        board.update(b)

        self.assertEqual(b.move_piece(Pos("a2")), False)

        b = Knight("ddd", Pos("b1"), board)
        board.update(b)

        self.assertEqual(b.move_piece(Pos("a3")), True)



if __name__ == "__main__":
    unittest.main()
