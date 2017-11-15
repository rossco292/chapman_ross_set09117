from enum import Enum #This is so that i can have an enum for selecting whos turn it is
#These are constants so that it is clear what i am using in my code
SYMBOL_KINGBLACK = 'B'
SYMBOL_KINGWHITE = 'W'
SYMBOL_EMPTY = 'E'
SYMBOL_BLACK = 'b'
SYMBOL_WHITE = 'w'
#This is essentially the "game board" and it is a list of lists which allows easy access to both rows and columns
Pieces = [["E","b","E","b","E","b","E","b"],["b","E","b","E","b","E","b","E"],["E","b","E","b","E","b","E","b"],["E","E","E","E","E","E","E","E"],
          ["E","E","E","E","E","E","E","E"],["w","E","w","E","w","E","w","E"],["E","w","E","w","E","w","E","w"],["w","E","w","E","w","E","w","E"]]
#This is where the enum is created in order to allow the turn to change
players = Enum("Players", "White Black")

def main():# This is the main where everything is essentially run
    Turns = dict([("Turn", players.Black)])# This sets the default turn to black
    print_board(Pieces)#This prints the board intially
    for i in range(100):# This is the loop that runs the game and it is set to 100 turns
        black_pawn_total = sum(x.count("b") for x in Pieces)# These four values are counting how many pieces are remaining of both kings and pawns for both players
        white_pawn_total = sum(y.count("w") for y in Pieces)
        black_king_total = sum(v.count("B") for v in Pieces)
        white_king_total = sum(z.count("W") for z in Pieces)
        white_total = white_king_total + white_pawn_total# In these 2 values the players kings and pawns are added together to get the total pieces each player has
        black_total = black_king_total + black_pawn_total
        if white_total == 0:#This if deals with the win condition
            print("Black player has won the game")
            qt = str(input("Do you want to quit the game y/n"))#This smaller if essentily asks if you want to quit the game so you can see who won
            if qt == "y":
                exit()
        if black_total == 0:#This if also deals with the win condition
            print("White player has won the game")
            qte = str(input("Do you want to quit the game y/n"))#This also asks if you want to quit the game
            if qte == "y":
                exit()
        print("total white pieces left", white_total)#Both these print functions allow the players to know how many pieces are left on either side
        print("total black pieces left" ,black_total)
        move(Turns, white_total, black_total, Pieces)#This calls the move function and passes in who's turn it is, the board and the two totals

def print_board(Pieces):#This function prints the board
    acc = 0#This accumulator allows the numbers at the side to be printed 
    print("    0    1    2    3    4    5    6    7")#This prints the column headers
    for row in Pieces:#This loops through the list of lists
        print(acc, row)
        acc = acc + 1#This accumulates to get every row

def move(Turns, white_total, black_total, Pieces):
    if Turns["Turn"] == players.Black:#These two ifs keep a record of whos turn it is so the players can see it
        print("It is currently black turn")
    if Turns["Turn"] == players.White:
        print("It is currently white turn")
        
    src_x = int(input("Enter an x coord to move from: "))#These 4 inputs are for both the 2 source coords and the 2 destination coords
    
    src_y = int(input("Enter a y coord to move from: "))
   
    dst_x = int(input("Enter an x coord to move to: "))
    
    dst_y = int(input("Enter a y coord to move to: "))
   
    if Pieces[src_y][src_x] == SYMBOL_EMPTY:#This checks if you have selected an empty square
        print("Empty cell")
        return
    midval_x = abs(src_x + dst_x) // 2#These get the middle value for when you jump over a piece
    midval_y = abs(src_y + dst_y) // 2
    if Turns["Turn"] == players.Black:#This checks who's turn it is
        
        if Pieces[src_y][src_x] == SYMBOL_WHITE or Pieces[src_y][src_x] == SYMBOL_KINGWHITE:
            print("Wrong piece selected try again ")
            print_board(Pieces)
            return move(Turns, white_total, black_total, Pieces)
#Movement logic
        if Pieces[src_y][src_x] == SYMBOL_BLACK and src_y > dst_y:
            print("Pawn cannot move backwards")
            return move(Turns, white_total, black_total, Pieces)
        if src_x == dst_x:
            print("You cant move a piece verticaly")
            return move(Turns, white_total, black_total, Pieces)
        if src_y == dst_y:
            print("You cant move a piece horizontaly")
            return move(Turns, white_total, black_total, Pieces)
        if dst_x > src_x + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_x < src_x - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_y > src_y + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_y < src_y - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
            
        
            
        if dst_y == 7:
            print("Congrats you have made a king Piece")
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            Pieces[7][dst_x] = SYMBOL_KINGBLACK
            return
            
        if Pieces[dst_y][dst_x] == SYMBOL_BLACK or Pieces[dst_y][dst_x] == SYMBOL_KINGBLACK:
            print("cannot move there as there is already one of your pieces there")
            return move(Turns, white_total, black_total, Pieces)
        
        if Pieces[dst_y][dst_x] == SYMBOL_WHITE or Pieces[dst_y][dst_x] == SYMBOL_KINGWHITE:
            print("cannot move there as there is already an opponents piece there")
            return move(Turns, white_total, black_total, Pieces)
        
        if Pieces[midval_y][midval_x] == SYMBOL_WHITE or Pieces[midval_y][midval_x] == SYMBOL_KINGWHITE:
            Pieces[midval_y][midval_x] = SYMBOL_EMPTY
            print_board(Pieces)
            return white_total

       
        
        if Pieces[src_y][src_x] == SYMBOL_BLACK:
            Pieces[dst_y][dst_x] = SYMBOL_BLACK
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)
            
        if Pieces[src_y][src_x] == SYMBOL_KINGBLACK:
            Pieces[dst_y][dst_x] = SYMBOL_KINGBLACK
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)
        Decision = str(input("Continue y/n?"))
        if Decision == "n":
            exit()
        
        Turns["Turn"] = players.White
        return 
        
    if Turns["Turn"] == players.White:
        
        if Pieces[src_y][src_x] == SYMBOL_BLACK:
            print("Wrong piece selected try again")
            print_board(Pieces)
            return move(Turns, white_total, black_total, Pieces)
        if Pieces[src_y][src_x] == SYMBOL_WHITE and src_y < dst_y:
            print("Pawn cannot move backwards")
            print_board(Pieces)
            return move(Turns, white_total, black_total, Pieces)
#Movement logic       
        if src_x == dst_x:
            print("You cant move a piece verticaly")
            return move(Turns, white_total, black_total, Pieces)
        if src_y == dst_y:
            print("You cant move a piece horizontaly")
            return move(Turns, white_total, black_total, Pieces)
        if dst_x > src_x + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_x < src_x - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_y > src_y + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)
        if dst_y < src_y - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total, Pieces)

        if dst_y == 0:
            print("Congrats you have made a king Piece")
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            Pieces[0][dst_x] = SYMBOL_KINGWHITE
            print_board(Pieces)
            return

        if Pieces[dst_y][dst_x] == SYMBOL_BLACK or Pieces[dst_y][dst_x] == SYMBOL_KINGBLACK:
            print("cannot move there as there is already one of your opponets pieces there")
            return move(Turns, white_total, black_total, Pieces)
        
        if Pieces[dst_y][dst_x] == SYMBOL_WHITE or Pieces[dst_y][dst_x] == SYMBOL_KINGWHITE:
            print("cannot move there as there is already one of your pieces there")
            return move(Turns, white_total, black_total, Pieces)
        
        if Pieces[midval_y][midval_x] == SYMBOL_BLACK or Pieces[midval_y][midval_x] == SYMBOL_KINGBLACK:
            Pieces[midval_y][midval_x] = SYMBOL_EMPTY
            print_board(Pieces)
           
            
        if Pieces[src_y][src_x] == SYMBOL_WHITE:
            Pieces[dst_y][dst_x] = SYMBOL_WHITE
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)
            
        
        if Pieces[src_y][src_x] == SYMBOL_KINGWHITE:
            Pieces[dst_y][dst_x] = SYMBOL_KINGWHITE
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)
        Decision = str(input("Continue y/n?"))
        if Decision == "n":
            exit()
        
        Turns["Turn"] = players.Black
        return
        
    
main()

        


        









