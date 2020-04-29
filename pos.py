from utils import algebra_to_cartesian, cartesian_to_algebra

class Pos:
    # _ means local methods that shouldnt be used in other classes
    knight_moves = {
        "LU": "self._lu(2,1)  ",
        "LD": "self._ld(2,1)",
        "RU": "self._ru(2,1)",
        "RD": "self._rd(2,1)",
        "UL": "self._lu(1,2)",
        "UR": "self._ru(1,2)",
        "DL": "self._ld(1,2)",
        "DR": "self._rd(1,2)",
    }
    diag_moves = {
        "LU": "self._lu(1,1)  ",
        "LD": "self._ld(1,1)",
        "RU": "self._ru(1,1)",
        "RD": "self._rd(1,1)",
    }
    # stored in dictionary format
    slide_moves = {
        "L": "self.left(1)  ",
        "R": "self.right(1)",
        "U": "self.up(1)",
        "D": "self.down(1)",
    }
    def __init__(self, coord):
        if isinstance(coord, tuple) or isinstance(coord, list):
            self.x = coord[0]
            self.y = coord[1]
            self.actualx = coord[0]
            self.actualy = coord[1]
        elif isinstance(coord, str):
            # Sorts out algebra to cartesian conversions
            self.x, self.y = algebra_to_cartesian(coord)
            self.actualx = self.x
            self.actualy = self.y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
            # tests whether classes are instances of one another
        else:
            return False

    def __str__(self):
        return (
            str(self.x)
            + ","
            + str(self.y)
            + " "
            + "".join(cartesian_to_algebra((self.x, self.y)))
        )

    def algebraic(self):
        return cartesian_to_algebra((self.actualx, self.actualy))

    def algebraic_newpos(self):
        return cartesian_to_algebra((self.x, self.y))

    def cartesian(self):
        return (self.actualx, self.actualy)

    def current(self):
        return [self.x, self.y]

    def left(self, num_moves, returnPath=False):
        # move left
        if 0 <= (self.x - num_moves) <= 7:
            self.x -= num_moves
        else:
            return False

    def right(self, num_moves, returnPath=False):
        if 0 <= self.x + num_moves <= 7:
            # its valid
            self.x += num_moves
        else:
            return False

    def up(self, num_moves, returnPath=False):
        if 0 <= self.y - num_moves <= 7:
            # its valid
            self.y -= num_moves
        else:
            return False

    def down(self, num_moves, returnPath=False):
        if 0 <= self.y + num_moves <= 7:
            self.y += num_moves
        else:
            return False

    #  return None
    def _lu(self, num_moves1, num_moves2):
        # move left and up
        if (0 <= (self.y - num_moves1) <= 7) and 0 <= self.x + -num_moves2 <= 7:

            self.y -= num_moves1
            self.x -= num_moves2
        else:
            return False

    def _ld(self, num_moves1, num_moves2):
        # move left and down

        if (0 <= (self.y + num_moves1) <= 7) and 0 <= self.x - num_moves2 <= 7:
            self.y += num_moves1
            self.x -= num_moves2
        else:
            return False

    def _ru(self, num_moves1, num_moves2):
        # move right and up

        if (0 <= (self.y - num_moves1) <= 7) and 0 <= self.x + num_moves2 <= 7:
            self.y -= num_moves1
            self.x += num_moves2
        else:
            return False

    def _rd(self, num_moves1, num_moves2):
        # move right and down

        if (0 <= (self.y + num_moves1) <= 7) and 0 <= self.x + num_moves2 <= 7:
            self.y += num_moves1
            self.x += num_moves2
        else:
            return False

    def diag(self, way, num_moves, piece=None, returnPath=True):
        list_of_moves = []
        for i in range(0, num_moves):
            prex, prey = self.x, self.y
            eval(self.diag_moves.get(way))
            if piece:
                # checks for pice collisions
                otherpiece, otherpiecename = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                if otherpiece:
                    # kills piece
                    if otherpiece.color != piece.color:
                        list_of_moves.append([self.x, self.y])
                        break
                    else:
                        break
            if prex == self.x and prey == self.y:
                break
            if returnPath:
                list_of_moves.append([self.x, self.y])
                # return the path taken for debugging purposes
        self.x = self.actualx
        self.y = self.actualy
        return list_of_moves

    def knight_hops(self, way, piece=None):
        # defnes knight moves and has similar styles to the bishop
        list_of_moves = []
        prex, prey = self.x, self.y
        eval(self.knight_moves.get(way))
        if prex == self.x and prey == self.y:
            return list_of_moves
        else:
            if piece:
                otherpiece, otherpiecename = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                if otherpiece:
                    if otherpiece.color != piece.color:
                        list_of_moves.append([self.x, self.y])
                else:
                    list_of_moves.append([self.x, self.y])

        self.x = self.actualx
        self.y = self.actualy
        return list_of_moves

    def slide(self, way, num_moves, piece=None, returnPath=True):
        # used for rook paths
        list_of_legal_moves = []
        for i in range(0, num_moves):
            prex, prey = self.x, self.y
            eval(self.slide_moves.get(way))
            if piece:
                obj, objname = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                if obj:
                    if obj.color != piece.color:
                        list_of_legal_moves.append([self.x, self.y])
                        break
                    else:
                        break

            if prex == self.x and prey == self.y:
                # using a buffer style
                break
            if returnPath:

                list_of_legal_moves.append([self.x, self.y])
        self.x = self.actualx
        self.y = self.actualy
        return list_of_legal_moves

    def samecolumn(self, way, newpos, num_moves):
        # checks if same column
        if (self.y - newpos.y) == num_moves:
            return True
        else:
            return False

    def samerow(self, way, newpos, num_moves=None):
        # checks if same row
        if self.y == newpos.y:
            return True
        else:
            return False

    def commit(self):
        # makes final changes and updates self
        self.actualx = self.x
        self.actualp = self.y
def test():

    posbr = Pos([7, 7])  # Bottom Right
    postl = Pos([0, 0])  # Top Left
    posbl = Pos([7, 0])  # Bottom Left
    postr = Pos([0, 7])  # Top Right
    print("Left Slide", postl.slide("L", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Right Slide", postl.slide("R", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Up Slide", postl.slide("U", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Down Slide", postl.slide("D", 3))
    print(pos.diag("LU", 3))
    print(pos.diag("LU", 2))
    print(pos.current())


# test()
