from utils import algebra_to_cartesian, cartesian_to_algebra

# The code to test
import unittest  # The test framework


class Test_Utils(unittest.TestCase):
    def test_conversion(self):
        self.assertEquals(cartesian_to_algebra([7, 0]), "h8")
        self.assertEquals(cartesian_to_algebra([0, 0]), "a8")
        self.assertEquals(cartesian_to_algebra([0, 7]), "a1")
        self.assertEquals(cartesian_to_algebra([7, 7]), "h1")
        self.assertEquals(cartesian_to_algebra([3, 3]), "d5")

    def test_conversion2(self):
        self.assertEquals(algebra_to_cartesian("h8"), (7, 0))
        self.assertEquals(algebra_to_cartesian("b8"), (1, 0))


if __name__ == "__main__":
    unittest.main()
