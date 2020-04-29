##Chess Engine##
########################################################
#TODO
#Make it classes

#Define the coord system

#dead file

class Board():

  def __init__():

    pass
  
  def show_board():
    pass
  



class Piece:
  def __init__(self, name, points, img, pos):
    self.name=name
    self.points=points
    self.img=img
    self.pos=pos
  
  def move_piece():
    pass
  

def coord_sys(coord):

  new_coord=[7-(int(coord[1])-1),(ord(coord[0])-97)]

  return new_coord

def all_pieces():

  black_knightb=Piece("black knight",3,"♘",coord_sys("b8"))
  black_knightg=Piece("black knight",3,"♘",coord_sys("g8"))
  #print(black_knightg.img)
  #print(black_knightb.pos)

  black_queen=Piece("black queen",9,"♕", coord_sys("d8"))

  black_king=Piece("black king", 0, "♔", coord_sys("e8"))

  black_rooka=Piece("black rook", 5, "♖", coord_sys("a8"))
  black_rookh=Piece("black rook", 5, "♖", coord_sys("h8"))

  black_bishopc=Piece("black bishop", 3, "♗", coord_sys("c8"))
  black_bishopf=Piece("black bishop", 3, "♗", coord_sys("f8"))

  black_pawna=Piece("black pawn", 1, "♙", coord_sys("a7"))
  black_pawnb=Piece("black pawn", 1, "♙", coord_sys("b7"))
  black_pawnc=Piece("black pawn", 1, "♙", coord_sys("c7"))
  black_pawnd=Piece("black pawn", 1, "♙", coord_sys("d7"))
  black_pawne=Piece("black pawn", 1, "♙", coord_sys("e7"))
  black_pawnf=Piece("black pawn", 1, "♙", coord_sys("f7"))
  black_pawng=Piece("black pawn", 1, "♙", coord_sys("g7"))
  black_pawnh=Piece("black pawn", 1, "♙", coord_sys("h7"))


  white_knightb=Piece("white knight",3,"♞",coord_sys("b1"))
  white_knightg=Piece("white knight",3,"♞",coord_sys("g1"))

  white_queen=Piece("white queen",9,"♛",coord_sys( "d1"))

  white_king=Piece("white king", 0, "♚", coord_sys("e1"))

  white_rooka=Piece("white rook", 5, "♜", coord_sys("a1"))
  white_rookh=Piece("white rook", 5, "♜",coord_sys( "h1"))

  white_bishopc=Piece("white bishop", 3, "♝", coord_sys("c1"))
  white_bishopf=Piece("white bishop", 3, "♝",coord_sys( "f1"))

  white_pawna=Piece("white pawn", 1, "♟", coord_sys("a2"))
  white_pawnb=Piece("white pawn", 1, "♟", coord_sys("b2"))
  white_pawnc=Piece("white pawn", 1, "♟", coord_sys("c2"))
  white_pawnd=Piece("white pawn", 1, "♟", coord_sys("d2"))
  white_pawne=Piece("white pawn", 1, "♟", coord_sys("e2"))
  white_pawnf=Piece("white pawn", 1, "♟", coord_sys("f2"))
  white_pawng=Piece("white pawn", 1, "♟", coord_sys("g2"))
  white_pawnh=Piece("white pawn", 1, "♟", coord_sys("h2"))



  def make_board():

  #spaces=[" ", " ", " ", " ", " "," "," ", " "]
 # board=[[black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook], [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],spaces,spaces,spaces,spaces, [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn], [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook]]
        
    board=[["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""]]


    #x=black_knightg.pos
    #print(x)
    board[black_knightb.pos[0]][black_knightb.pos[1]]=black_knightb.img
    board[black_knightg.pos[0]][black_knightg.pos[1]]=black_knightg.img
    board[black_queen.pos[0]][black_queen.pos[1]]=black_queen.img
    board[black_king.pos[0]][black_king.pos[1]]=black_king.img
    board[black_rooka.pos[0]][black_rooka.pos[1]]=black_rooka.img
    board[black_rookh.pos[0]][black_rookh.pos[1]]=black_rookh.img
    board[black_bishopc.pos[0]][black_bishopc.pos[1]]=black_bishopc.img
    board[black_bishopf.pos[0]][black_bishopf.pos[1]]=black_bishopf.img  
    board[black_pawna.pos[0]][black_pawna.pos[1]]=black_pawna.img
    board[black_pawnb.pos[0]][black_pawnb.pos[1]]=black_pawnb.img
    board[black_pawnc.pos[0]][black_pawnc.pos[1]]=black_pawnc.img
    board[black_pawnd.pos[0]][black_pawnd.pos[1]]=black_pawnd.img
    board[black_pawne.pos[0]][black_pawne.pos[1]]=black_pawne.img
    board[black_pawnf.pos[0]][black_pawnf.pos[1]]=black_pawnf.img
    board[black_pawng.pos[0]][black_pawng.pos[1]]=black_pawng.img
    board[black_pawnh.pos[0]][black_pawnh.pos[1]]=black_pawnh.img
  
    board[white_knightb.pos[0]][white_knightb.pos[1]]=white_knightb.img
    board[white_knightg.pos[0]][white_knightg.pos[1]]=white_knightg.img
    board[white_queen.pos[0]][white_queen.pos[1]]=white_queen.img
    board[white_king.pos[0]][white_king.pos[1]]=white_king.img
    board[white_rooka.pos[0]][white_rooka.pos[1]]=white_rooka.img
    board[white_rookh.pos[0]][white_rookh.pos[1]]=white_rookh.img
    board[white_bishopc.pos[0]][white_bishopc.pos[1]]=white_bishopc.img
    board[white_bishopf.pos[0]][white_bishopf.pos[1]]=white_bishopf.img
    board[white_pawna.pos[0]][white_pawna.pos[1]]=white_pawna.img
    board[white_pawnb.pos[0]][white_pawnb.pos[1]]=white_pawnb.img
    board[white_pawnc.pos[0]][white_pawnc.pos[1]]=white_pawnc.img
    board[white_pawnd.pos[0]][white_pawnd.pos[1]]=white_pawnd.img
    board[white_pawne.pos[0]][white_pawne.pos[1]]=white_pawne.img
    board[white_pawnf.pos[0]][white_pawnf.pos[1]]=white_pawnf.img
    board[white_pawng.pos[0]][white_pawng.pos[1]]=white_pawng.img
    board[white_pawnh.pos[0]][white_pawnh.pos[1]]=white_pawnh.img

    
    #print(board)

    for row in board:
      #print("a"+row)
      print(' | '.join([str(elem) for elem in row]))
      
    #print()
  make_board()



# if we visualise the chess board as a 8*8 matrix, where it is positioned in the positive quadrant of a cartesian plane

#let the position of a piece be a cartesian coordinate, stored as a tuple e.g. [i,j] for x and y
    

#8|
#7|p  p  p  p  p  p  p  p
#6|
#5|
#4|
#3|
#2|p  p  p  p  p  p  p  p 
#1|r  h  b  q  k  b  h  r
#  [1][2][3][4][5][6][7][8]



all_pieces()


def rules():
  def pawn_moves(pawn_position):

    new_pawn_position=[]
    if int(pawn_position[0]) ==" " and int(pawn_position[1])+1==" ":
      #pawn can be moved 1 step forward
      new_pawn_position= [pawn_position[0], (pawn_position[1]+1)]

      return new_pawn_position
    # TODO: check the moves history if its the first move because then it can move up to 2 spaces

  def bishop_moves(bishop_position):
    pass
  
  def knight_moves():
    pass

  def rook_moves():
    pass

  def king_moves():
    pass

  def queen_moves():
    pass




#make_board()
#rules()