from pieces import Pawn
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_Pawn(unittest.TestCase):
    def test_Pawn1(self):
        board = Board()
        Board.populateBoard(board)
        """
        b = Pawn("black pawna", Pos("a7"), board)
        self.assertEqual(b.move_piece(Pos("a6")), True)

        b = Pawn("black pawna", Pos("a5"), board)
        self.assertEqual(b.move_piece(Pos("a6")), False)

        b = Pawn("white pawna", Pos("a2"), board)
        self.assertEqual(b.move_piece(Pos("a4")), True)

        b = Pawn("white pawna", Pos("a7"), board)
        self.assertEqual(b.move_piece(Pos("a5")), False)
        """
        b = Pawn("black pawna", Pos("e5"), board)
        board.update(b)

        w = Pawn("white pawna", Pos("d4"), board)
        board.update(w)

        self.assertEqual(b.move_piece(Pos("d4")), True)



if __name__ == "__main__":
    unittest.main()
