from pos import Pos
from board import Board
from utils import algebra_to_cartesian, cartesian_to_algebra

# The code to test
import unittest  # The test framework


class Test_Pos(unittest.TestCase):
    def test_diag_LU(self):

        self.assertEquals(Pos(algebra_to_cartesian("a1")).diag("LU", 5), [])
        self.assertEquals(Pos(algebra_to_cartesian("a8")).diag("LU", 5), [])


        print(Pos(algebra_to_cartesian("h8")).diag("LU", 5))
        self.assertEquals(Pos(algebra_to_cartesian("h8")).diag("LU", 5), [])

    def test_diag_RU(self):

        self.assertEquals(
            Pos(algebra_to_cartesian("a1")).diag("RU", 5),
            [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2]],
        )
        self.assertEquals(Pos(algebra_to_cartesian("a8")).diag("RU", 5), [])

        self.assertEquals(Pos(algebra_to_cartesian("h1")).diag("RU", 5), [])

        self.assertEquals(Pos(algebra_to_cartesian("h8")).diag("RU", 5), [])

    def test_pos_slide_withboard(self):
        pos = Pos("a3")
        print(pos.slide("U", 3))


        board = Board()
        board.populateBoard()

        pos = Pos("a1")
        print(pos.slide("U", 2, board))


        pos = Pos("h1")
        print(pos.slide("U", 2, board))


    def test_knight_hops(self):

        self.assertEquals(Pos(algebra_to_cartesian("b1")).knight_hops("RU"), [[2, 5]])

        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("RD"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("RU"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("LU"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("LD"))


if __name__ == "__main__":
    unittest.main()
