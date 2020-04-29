import pygame
# imports externel package
from pos import Pos
from utils import cartesian_to_algebra, algebra_to_cartesian
from board import Board

class Uiboard:
    def __init__(self):
        # set color with rgb
        self.white, self.black, self.red = (255, 255, 255), (150, 150, 150), (255, 0, 0)
        # set display
        self.gameDisplay = pygame.display.set_mode((800, 700))
        # caption
        # beginning of logic
        self.gameExit = False
        self.size = 60
        pygame.init()
        pygame.display.set_caption("ChessBoard")
        self.font = pygame.font.Font("freesansbold.ttf", 12)
        self.gameDisplay.fill(self.white)
        self.textX, self.textY = 600, 60
        self.errTextX, self.errTextY = 100, 600
        # board length, must be even
        self.boardLength = 8
    def drawEmptyBoard(self):
        """ Setup the basic chess board """
        cnt = 0
        for i in range(1, self.boardLength + 1):
            for z in range(1, self.boardLength + 1):
                # check if current loop value is even
                if cnt % 2 == 0:
                    pygame.draw.rect(
                        self.gameDisplay,
                        self.white,
                        [self.size * z, self.size * i, self.size, self.size],
                    )
                else:
                    pygame.draw.rect(
                        self.gameDisplay,
                        self.black,
                        [self.size * z, self.size * i, self.size, self.size],
                    )
                cnt += 1
            # since theres an even number of squares go back one value
            cnt -= 1
        # Add a nice border
        pygame.draw.rect(
            self.gameDisplay,
            self.black,
            [
                self.size,
                self.size,
                self.boardLength * self.size,
                self.boardLength * self.size,
            ],
            1,
        )
        pygame.display.update()

    def gameOn(self, board):
        """ This method has a while loop  until game exit is called"""
        # contains main logic and connections
        self.paintBoard(board)
        # paints the board after every change
        lastColor = "black"
        # only white goes first
        selectedPiece = None
        orgpos = None
        board.storeOnFile()
        # opens file for storing
        while not self.gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()
                    # quits game

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    newpos = self.eventpos_to_algebraic(mousepos)
                    # clicks on piece
                    if selectedPiece:
                        # previous click selected the piece
                        orgpos = selectedPiece.currpos
                        valid_move = selectedPiece.move_piece(Pos(newpos))
                        self.paintErrorText("                                                                       ")

                        if valid_move:
                            # only update if its a valid move
                            board.updateMoveOnFile(
                                selectedPiece,
                                str(
                                    "".join(cartesian_to_algebra((orgpos.x, orgpos.y)))
                                ),
                                newpos,
                            )
                        else: 
                            selectedPiece=None
                        if valid_move:
                            self.paintBoard(board)
                            colors2 = ["white", "black"]
                            colors2.remove(lastColor)
                            # shows which color piece just went
                            print("last color", str(colors2[0]))
                            
                            self.paintMoveText(
                                str(colors2[0])
                                + " : "
                                + str(
                                    "".join(cartesian_to_algebra((orgpos.x, orgpos.y)))
                                )
                                + " "
                                + str(newpos)
                            )
                            print("".join(cartesian_to_algebra((orgpos.x, orgpos.y))))

                            lastColor = selectedPiece.color
                            selectedPiece = None
                        else:

                            self.paintErrorText("Invalid Move")
                    else:
                        # this click is the first click
                        currentPiece, _ = board.piece_from_algebraic_coord(newpos)
                        if currentPiece:
                            selectedPiece = currentPiece
                        else:
                            continue
                        if lastColor:
                            if currentPiece.color != lastColor:
                                selectedPiece = currentPiece
                            else:

                                # Could use a enum for string
                                colors1 = ["white", "black"]
                                colors1.remove(lastColor)
                                self.paintErrorText(
                                    "Please select a %s piece" % str(colors1[0])
                                )
                                selectedPiece = None
                               
            pygame.display.update()

    def eventpos_to_algebraic(self, pos):
        # returns the mouse coords into algebraic coords
        x = (pos[0] - 60) // 60
        y = (pos[1] - 60) // 60
        alg = cartesian_to_algebra((x, y))
        return alg

    def paintBoard(self, board: Board):
        """ Given any board it will blit the positions 
            Requires the pieces in the board to have specific names so that 
            the png paths can be found
        """
        self.drawEmptyBoard()
        for posstr, piece in board.pieceByPosDict.items():
            # places pieces on board
            print(posstr, piece)
            res = piece.name.split("_")
            print(res)
            pngpath = "_".join([res[0], res[1]])
            displayimg = pygame.image.load("ui\\%s.png" % (pngpath))  # from piece
            X, Y = algebra_to_cartesian(posstr)
            print((X + 1) * 60, (Y + 1) * 60)
            self.gameDisplay.blit(displayimg, ((X + 1) * 60, (Y + 1) * 60))

    def paintMoveText(self, alg: str):
        """ Paints a string , keeps the latest position updated """
        text = self.font.render(alg, True, self.black, self.white)
        textRect = text.get_rect()
        textRect.center = (self.textX, self.textY)
        self.gameDisplay.blit(text, textRect)
        print(self.textX, self.textY)
        self.textY += 15

    def paintErrorText(self, errorString: str):
        """ Paints a string , keeps the latest position updated """
        text = self.font.render(errorString, True, self.black, self.white)
        textRect = text.get_rect()
        textRect.center = (self.errTextX, self.errTextY)
        self.gameDisplay.blit(text, textRect)
        print(self.errTextX, self.errTextY)

CHESSPIECEDICT = {}

if __name__ == "__main__":
    # view
    uiboard = Uiboard()
    # model
    board = Board()
    board.populateBoard()
    uiboard.gameOn(board)
