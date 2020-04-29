from pieces import Bishop
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework

class Test_Bishop(unittest.TestCase):
    def test_Bishop1(self):
        board = Board()
        Board.populateBoard(board)


        b = Bishop("ddd", Pos("c5"), board)
        board.update(b)

        self.assertEqual(b.move_piece(Pos("h3")), False)

        b = Bishop("ddd", Pos("c5"), board)
        board.update(b)

        self.assertEqual(b.move_piece(Pos("d4")), True)


if __name__ == "__main__":
    unittest.main()
