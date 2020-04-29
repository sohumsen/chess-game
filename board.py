from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King
from utils import algebra_to_cartesian, cartesian_to_algebra
from pos import Pos
import datetime

spaceConstant = " "
class Board:

    """
    A datastructure that looks like 
    board = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
    ]

    """
    def __init__(self, *args, **kwargs):
        # the boards data that stores the piece positions
        self.screen = [[spaceConstant] * 8 for i in range(8)]
        # dict of pos to pieceObj
        self.pieceByPosDict = {}

    def setScreen(self, i, j, val):
        self.screen[j][i] = val

    def update(self, piece, newPosObj=None):
        # paints the board

        if not newPosObj:
            newPosObj = piece.currpos
            #changes the pos object

        self.setScreen(piece.currpos.x, piece.currpos.y, spaceConstant)
        self.setScreen(newPosObj.x, newPosObj.y, piece.img)

        # keeps the data structures in shape
        self.pieceByPosDict.pop(piece.currpos.algebraic(), None)
        self.pieceByPosDict[newPosObj.algebraic()] = piece

    def populateBoard(self):
        """ Populates the board array"""
        self.pieceByPosDict = {
            "b8": Knight("black_knight_b", Pos("b8")),
            "g8": Knight("black_knight_g", Pos("g8")),
            "d8": Queen("black_queen", Pos("d8")),
            "e8": King("black_king", Pos("e8")),
            "a8": Rook("black_rook_a", Pos("a8")),
            "h8": Rook("black_rook_h", Pos("h8")),
            "c8": Bishop("black_bishop_c", Pos("c8")),
            "f8": Bishop("black_bishop_f", Pos("f8")),
            "a7": Pawn("black_pawn_a", Pos("a7")),
            "b7": Pawn("black_pawn_b", Pos("b7")),
            "c7": Pawn("black_pawn_c", Pos("c7")),
            "d7": Pawn("black_pawn_d", Pos("d7")),
            "e7": Pawn("black_pawn_e", Pos("e7")),
            "f7": Pawn("black_pawn_f", Pos("f7")),
            "g7": Pawn("black_pawn_g", Pos("g7")),
            "h7": Pawn("black_pawn_h", Pos("h7")),
            "b1": Knight("white_knight_b", Pos("b1")),
            "g1": Knight("white_knight_g", Pos("g1")),
            "d1": Queen("white_queen", Pos("d1")),
            "e1": King("white_king", Pos("e1")),
            "a1": Rook("white_rook_a", Pos("a1")),
            "h1": Rook("white_rook_h", Pos("h1")),
            "c1": Bishop("white_bishop_c", Pos("c1")),
            "f1": Bishop("white_bishop_f", Pos("f1")),
            "a2": Pawn("white_pawn_a", Pos("a2")),
            "b2": Pawn("white_pawn_b", Pos("b2")),
            "c2": Pawn("white_pawn_c", Pos("c2")),
            "d2": Pawn("white_pawn_d", Pos("d2")),
            "e2": Pawn("white_pawn_e", Pos("e2")),
            "f2": Pawn("white_pawn_f", Pos("f2")),
            "g2": Pawn("white_pawn_g", Pos("g2")),
            "h2": Pawn("white_pawn_h", Pos("h2")),
        }

        # Let pieces have a reference to the board
        for key, pieceObj in self.pieceByPosDict.items():
            pieceObj.board = self

        # update the screen datastructure
        for keyStr, pieceObj in self.pieceByPosDict.items():
            pos = Pos(keyStr)
            self.setScreen(pos.x, pos.y, pieceObj.img)

    def piece_from_algebraic_coord(self, coordStr):

        obj = self.pieceByPosDict.get(coordStr, None)
        #finds the piece, given a coordinate

        if obj:
            return obj, obj.name
        else:
            return None, spaceConstant

    def __str__(self):
        return "This is a board "
        #accessed by printing the object

    def printBoardOnScreen(self):

        for i in range(0, len(self.screen)):
            for j in range(0, len(self.screen[i])):
                if ord(self.screen[j][i]) < 9812 or ord(self.screen[j][i]) > 9823:
                    #prints the board on the command line rather than GUI, in case they dont have pygame
                    self.screen[j][i] = " "

        for i in range(0, 8):
            print(
                str(8 - i)
                + "| "
                + (" | ".join([str(elem) for elem in self.screen[i]]))
                + " |"
            )
        print("   a   b   c   d   e   f   g   h")
        #prints the edges

    def storeOnFile(self):
        f = open("pastgames.txt", "a")
        f.write(" \n" + str(datetime.datetime.now()) + " \n")
        f.close()
        #opens the past games text file and writes the date

    def updateMoveOnFile(self, pieceObj, curr_algebraic_coord, next_algebraic_coord):
        f = open("pastgames.txt", "a")
        f.write(
            pieceObj.color.upper()
            + " : "
            + str(curr_algebraic_coord)
            + " "
            + str(next_algebraic_coord)
            + " \n"
        )
        f.close()
        #opens the past games text file and writes the moveset
