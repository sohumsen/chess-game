from pieces import Bishop
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException

# The code to test
import unittest  # The test framework
from pieces import Knight, Rook
from pos import Pos


class Test_Board(unittest.TestCase):
    def test_board(self):
        board = Board()
        board.populateBoard()

        p = Knight("ddd", Pos("b8"), board)
        board.update(p, Pos("a4"))  # bypasses the move piece allows illegal moves
        board.printBoardOnScreen()
        obj, objname = board.piece_from_algebraic_coord("a4")
        self.assertIsInstance(obj, Knight)
        print(obj)

    def test_retrievePiece(self):
        board = Board()
        board.populateBoard()
        board.printBoardOnScreen()
        obj, objname = board.piece_from_algebraic_coord("a1")
        self.assertIsInstance(obj, Rook)
        expected_pos = Pos("a1")
        self.assertEqual(obj.currpos, expected_pos)


if __name__ == "__main__":
    unittest.main()
