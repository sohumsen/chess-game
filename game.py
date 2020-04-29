from board import Board
from uiboard import Uiboard
from utils import algebra_to_cartesian
from pos import Pos
import datetime

def move(color):
    validMove = False
    # only enters while loop if its a valid move
    while not validMove:
        print("%s moves now: " % color.upper())
        currAlgebraicCoord = input("Enter the current piece location >")

        nextAlgebraicCoord = input("Enter the goto location >")

        if currAlgebraicCoord == "end" or nextAlgebraicCoord == "end":
            break
            # type end to exit the program in command line
        pieceObj, _ = board.piece_from_algebraic_coord(currAlgebraicCoord)
        if pieceObj:  # there is a piece there
            if pieceObj.color == color:
                validMove = pieceObj.move_piece(Pos(nextAlgebraicCoord))
                # pieces are the same color
                if validMove:
                    board.updateMoveOnFile(
                        color, currAlgebraicCoord, nextAlgebraicCoord
                    )
                    # update the file
                if not validMove:
                    # not a valid move
                    # raise exception
                    print(
                        "Invalid move "
                        + currAlgebraicCoord
                        + " cannot move to "
                        + nextAlgebraicCoord
                    )
            else:
                print("%s moves " % color.upper())
        else:
            print("No object at that place")
        Board.printBoardOnScreen(board)
        # prints the board array on a command line

def readfile():
    # opens past game file
    f = open("pastgames.txt", "r")
    print(f.read())
    f.close()

def mainMenu():
    validChoice = False
    while not validChoice:
        choice = int(
            input("Enter a choice: \n 1) Player v Player \n 2) Review past games \n")
        )
        if choice == 1:
            # for p v p
            validChoice = True
            board.populateBoard()
            board.printBoardOnScreen()
            # to play on command line, hash the next line
            uiboard.gameOn(board)
            board.storeOnFile()
            while True:
                move("white")
                move("black")

        elif choice == 2:
            # for reading files
            validChoice = True
            readfile()
        else:
            print("Enter a valid choice")
    pass

if __name__ == "__main__":
    uiboard = Uiboard()
    board = Board()
    #initialises the board and uiboard
    while True:
        mainMenu()
