SIZE_H = 8
SIZE_W = 8
SYMBOL_EMPTY = 'E'
SYMBOL_BLACK = 'B'
SYMBOL_WHITE = 'W'
Pieces = [["E","B","E","B","E","B","E","B"],["B","E","B","E","B","E","B","E"],["E","B","E","B","E","B","E","B"],["E","E","E","E","E","E","E","E"],
          ["E","E","E","E","E","E","E","E"],["W","E","W","E","W","E","W","E"],["E","W","E","W","E","W","E","W"],["W","E","W","E","W","E","W","E"]]



    
def print_board(Pieces):
    acc = 0
    print("    0    1    2    3    4    5    6    7")
    for row in Pieces:
        print(acc, row)
        acc = acc + 1

def move():
    src_x = int(input("Enter an x coord to move from: "))
    src_y = int(input("Enter a y coord to move from: "))
    dst_x = int(input("Enter an x coord to move to: "))
    dst_y = int(input("Enter a y coord to move to: "))
    black_score = 0
    white_score = 0
    x_diff = (src_x - dst_x)
    y_diff = (src_y - dst_y)
    #if sorted([y_diff, x_diff]) != [2, 2] or [1, 1] or [-2, -2] or [-1, -1] or [-2, 2] or [2, -2] or [-1, 1] or [1, -1]:
        #print("incorrect coords")
        #return
    if Pieces[src_y][src_x] == SYMBOL_EMPTY:
        print("Empty cell")
        return
    midval_x = (src_x + dst_x) // 2
    midval_y = (src_y + dst_y) // 2
    if Pieces[midval_y][midval_x] == SYMBOL_WHITE:
        black_score = black_score + 1
        Pieces[midval_y][midval_x] = SYMBOL_EMPTY
        return
    if Pieces[src_y][src_x] == SYMBOL_BLACK:
        Pieces[dst_y][dst_x] = SYMBOL_BLACK
        Pieces[src_y][src_x] = SYMBOL_EMPTY
        return
    if Pieces[src_y][src_x] == SYMBOL_WHITE:
        Pieces[dst_y][dst_x] = SYMBOL_WHITE
        Pieces[src_y][src_x] = SYMBOL_EMPTY
        return
    

def main():
    turncount = 0
    movebl = True
    movew = True
    for i in range(100):
        turncount = turncount + 1
        if movebl == True:
            print(turncount)
            print_board(Pieces)
            move()
        if turncount == 3:
            break
        


        









