from utils import algebra_to_cartesian, cartesian_to_algebra
from exceptions import InvalidMoveException
from pos import Pos
import copy

# creates the piece class
class Piece:
    def __init__(self, name, posobj, board=None):
        self.name = name
        if self.name.find("white") == -1:
            # if the name doesnt have white, then the color of the piece must be black
            self.color = "black"
        else:
            self.color = "white"

        self.board = board
        self.currpos = posobj
        self.newpos = posobj
        self.img = None

    def move_piece(self, newPosObj):
        # contains move validation
        self.newpos = newPosObj
        # sets a new piece position
        validMove = self.validate_move()
        if validMove == True:  # and no piece there
            self.updateBoardAndPiece()
            return True
        else:
            print("Invalid Move")
            return False

    def updateBoardAndPiece(self):
        """ works for any piece """
        self.board.update(self, self.newpos)
        self.currpos = self.newpos

    def getMovements(self):
        """ returns the old and new positions"""
        return self.currpos, self.newpos

class Pawn(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        # uses inheritance to gain attributes of its super class
        self.points = 1
        if "black" in self.name:
            self.img = "♙"
            # uses the black pawn image
        else:
            self.img = "♟"

    def move_piece(self, newPosObj):
        self.newpos = newPosObj
        # sets the coordinate as a position object
        validMove = False
        # initialise validMove
        obj, objname = self.board.piece_from_algebraic_coord(newPosObj.algebraic())
        # find the piece object at a specific location
        # Normal Pawn Movements
        if self.currpos.x == self.newpos.x:
            if not obj:
                if self.color == "white":
                    if self.currpos.y == 6:
                        if self.currpos.samecolumn(
                            "U", self.newpos, 2
                        ) or self.currpos.samecolumn("U", self.newpos, 1):
                            validMove = True
                    else:
                        if self.currpos.samecolumn("U", self.newpos, 1):
                            validMove = True

                elif self.color == "black":
                    if self.currpos.y == 1:
                        if self.currpos.samecolumn(
                            "U", self.newpos, -2
                        ) or self.currpos.samecolumn("U", self.newpos, -1):
                            validMove = True
                    else:
                        if self.currpos.samecolumn("U", self.newpos, -1):
                            validMove = True
        # kill another pawn
        else:
            # theres a piece from a diff color
            if obj and self.color != obj.color:
                if self.color == "white" and self.newpos.y + 1 == self.currpos.y:
                    if (self.currpos.x + 1 == self.newpos.x) or (
                        self.currpos.x - 1 == self.newpos.x
                    ):
                        validMove = True
                elif self.color == "black" and self.newpos.y - 1 == self.currpos.y:
                    if (self.currpos.x + 1 == self.newpos.x) or (
                        self.currpos.x - 1 == self.newpos.x
                    ):
                        validMove = True

        if validMove == True:
            # and no piece there
            self.updateBoardAndPiece()
            return True
        else:

            print("FAIL")
            # its not a valid move
            return False

class Knight(Piece):
    def __init__(self, name, posobj, board=None):
        # it used to have Board
        super().__init__(name, posobj, board)
        # uses inheritance of superclass
        self.points = 3
        if "black" in name:

            self.img = "♘"
        else:
            self.img = "♞"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        # copy the position coordinates and its attributes into another variable
        allmoves = []
        print(pos)
        print(self.currpos)
        for way in pos.knight_moves.keys():
            # finds the list of possible moves
            allmoves.extend(pos.knight_hops(way, self))
        print(allmoves)
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True
                # its a valid move, since its in the allmoves dictionary
        return False

class Bishop(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 3
        if "black" in self.name:

            self.img = "♗"
        else:
            self.img = "♝"

    def validate_move(self):
        pos = copy.deepcopy(self.currpos)
        print(pos)
        allmoves = []
        # gets all the pathways of the possible moves
        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 7, self, self.board))
            # specific to bishops
            print(way, pos, allmoves)
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True
        return False

class Rook(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 5
        if "black" in self.name:
            self.img = "♖"
        else:
            self.img = "♜"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        allmoves = []
        # gets all the pathways of the possible moves
        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 7, self))
        print(pos, allmoves)
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                # the move is legal
                return True
                # is there a piece in the way
                break
        return False

class Queen(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 9
        if "black" in self.name:
            self.img = "♕"
        else:
            self.img = "♛"

    def validate_move(self):
        pos = copy.deepcopy(self.currpos)
        allmoves = []
        # gets all the pathways of the possible moves
        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 7, self))
            print(way, pos, allmoves)
        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 7, self))
            print(way, pos, allmoves)
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True
        return False

class King(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 100
        if "black" in self.name:
            self.img = "♔"
        else:
            self.img = "♚"

    def validate_move(self):
        pos = copy.deepcopy(self.currpos)
        print(pos)
        allmoves = []
        castle = []
        # gets all the pathways of the possible moves
        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 1, self))
            print(way, pos, allmoves)
        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 1, self))
            print(way, pos, allmoves)
        if self.color == "white" and self.currpos.current == [4, 7]:
            # enables castling
            obj1, objname1 = self.board.piece_from_algebraic_coord("h1")
            obj2, objname2 = self.board.piece_from_algebraic_coord("a1")
            if objname1 == "white rook h":
                allmoves.extend(pos.diag("R", 3, self))
                # there is a path
            if objname2 == "white rook a":
                # if obj
                allmoves.extend(pos.diag("L", 4, self))
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True

        return False

if __name__ == "__main__":
    # a optimisation test
    def f2():
        kn = Knight("ddd", 3, "", algebra_to_cartesian("b8"), None)
        for i in range(0, 7):
            for j in range(0, 7):
                kn.newpos.x = i
                kn.newpos.y = j
                kn.validateMove()
        return
