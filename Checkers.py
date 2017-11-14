from enum import Enum
import json
SYMBOL_KINGBLACK = 'B'
SYMBOL_KINGWHITE = 'W'
SYMBOL_EMPTY = 'E'
SYMBOL_BLACK = 'b'
SYMBOL_WHITE = 'w'
Undosource_x = 0
Undosource_y = 0
Undodestin_x = 0
Undodestin_y = 0
black_total = 12
white_total = 12
Pieces = [["E","b","E","b","E","b","E","b"],["b","E","b","E","b","E","b","E"],["E","b","E","b","E","b","E","b"],["E","E","E","E","E","E","E","E"],
          ["E","E","E","E","E","E","E","E"],["w","E","w","E","w","E","w","E"],["E","w","E","w","E","w","E","w"],["w","E","w","E","w","E","w","E"]]

players = Enum("Players", "White Black")

def main():
    Turns = dict([("Turn", players.Black)])
    for i in range(100):
        Decision = str(input("Exit or move?"))
        if Decision == "Exit":
            exit()
        print_board(Pieces)
        move(Turns, white_total, black_total, Pieces)
        



    

def print_board(Pieces):
    acc = 0
    print("    0    1    2    3    4    5    6    7")
    for row in Pieces:
        print(acc, row)
        acc = acc + 1

def move(Turns, white_total, black_total, Pieces):
    if Turns["Turn"] == players.Black:
        print("It is currently black turn")
    if Turns["Turn"] == players.White:
        print("It is currently white turn")
    src_x = int(input("Enter an x coord to move from: "))
    src_y = int(input("Enter a y coord to move from: "))
    dst_x = int(input("Enter an x coord to move to: "))
    dst_y = int(input("Enter a y coord to move to: "))
    x_diff = abs(src_x - dst_x)
    y_diff = abs(src_y - dst_y)
    if black_total == 0:
        print("White player wins")
        exit()
    if white_total == 0:
        print("Black player wins")
        exit()
    if Pieces[src_y][src_x] == SYMBOL_EMPTY:
        print("Empty cell")
        return
    midval_x = abs(src_x + dst_x) // 2
    midval_y = abs(src_y + dst_y) // 2
    if Turns["Turn"] == players.Black:
        Decision = str(input("Exit or move or undo?"))
        if Decision == "Exit":
            exit()
                           
        if Pieces[src_y][src_x] == SYMBOL_WHITE or Pieces[src_y][src_x] == SYMBOL_KINGWHITE:
            print("Wrong piece selected try again ")
            print_board(Pieces)
            return move(Turns, white_total, black_total)
#Movement logic
        if Pieces[src_y][src_x] == SYMBOL_BLACK and src_y > dst_y:
            print("Pawn cannot move backwards")
            return move(Turns, white_total, black_total)
        if src_x == dst_x:
            print("You cant move a piece verticaly")
            return move(Turns, white_total, black_total)
        if src_y == dst_y:
            print("You cant move a piece horizontaly")
            return move(Turns, white_total, black_total)
        if dst_x > src_x + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_x < src_x - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_y > src_y + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_y < src_y - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
            
        
            
        if dst_y == 7:
            print("Congrats you have made a king Piece")
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            Pieces[7][dst_x] = SYMBOL_KINGBLACK
            return
            
       
        if Pieces[midval_y][midval_x] == SYMBOL_WHITE or Pieces[midval_y][midval_x] == SYMBOL_KINGWHITE:
            Pieces[midval_y][midval_x] = SYMBOL_EMPTY
            white_total = white_total - 1
            print("This is how many white pieces are left: ", white_total)

        if Pieces[midval_y][midval_x] == SYMBOL_EMPTY:
            print("cant jump over nothing")
            return move(Turns, white_total, black_total)
        
        if Pieces[src_y][src_x] == SYMBOL_BLACK:
            Pieces[dst_y][dst_x] = SYMBOL_BLACK
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)

        if Pieces[src_y][src_x] == SYMBOL_KINGBLACK:
            Pieces[dst_y][dst_x] = SYMBOL_KINGBLACK
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            print_board(Pieces)
            
        Turns["Turn"] = players.White
        return 
        
    if Turns["Turn"] == players.White:
        Decision = str(input("Exit or move or undo?"))
        if Decision == "Exit":
            exit()
        if Pieces[src_y][src_x] == SYMBOL_BLACK:
            print("Wrong piece selected try again")
            print_board(Pieces)
            return move(Turns, white_total, black_total)
        if Pieces[src_y][src_x] == SYMBOL_WHITE and src_y < dst_y:
            print("Pawn cannot move backwards")
            return move(Turns, white_total, black_total)
#Movement logic       
        if src_x == dst_x:
            print("You cant move a piece verticaly")
            return move(Turns, white_total, black_total)
        if src_y == dst_y:
            print("You cant move a piece horizontaly")
            return move(Turns, white_total, black_total)
        if dst_x > src_x + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_x < src_x - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_y > src_y + 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)
        if dst_y < src_y - 2:
            print("You cant move farther than 2 spaces in a jump")
            return move(Turns, white_total, black_total)

        if dst_y == 0:
            print("Congrats you have made a king Piece")
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            Pieces[0][dst_x] = SYMBOL_KINGWHITE
            return
        if Pieces[midval_y][midval_x] == SYMBOL_BLACK or Pieces[midval_y][midval_x] == SYMBOL_KINGBLACK:
            Pieces[midval_y][midval_x] = SYMBOL_EMPTY
            black_total = black_total - 1
            print("This is how many black pieces are left: ", black_total)
            
        if Pieces[src_y][src_x] == SYMBOL_WHITE:
            Pieces[dst_y][dst_x] = SYMBOL_WHITE
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            
        if Pieces[src_y][src_x] == SYMBOL_KINGWHITE:
            Pieces[dst_y][dst_x] = SYMBOL_KINGWHITE
            Pieces[src_y][src_x] = SYMBOL_EMPTY
            
        Turns["Turn"] = players.Black
        return
        
    
main()

        


        









