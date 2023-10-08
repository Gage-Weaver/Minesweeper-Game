#Minesweeper game
import random
def boardcreation():
    rows = 0
    columns = 0
    mines = 0
    while rows < 1:
        try:
            rows = int(input('Input the amount of rows you would like to play with (Whole Number): '))
        except:
            print('The amount of rows must be a whole number')
            pass
    while columns < 1:
        try:
            columns = int(input('Input the amount of columns you would like to play with (Whole Number): '))
        except:
            print('The amount of columns must be a whole number')
            pass
    while mines < 1:
        try:
            mines = int(input('Input the amount of mines you would like to play with (Whole Number): '))
            if mines > rows*columns:
                mines = 0
                print('You cannot have more mines than spaces on the board')
        except:
            print('The amount of mines must be a whole number')
            pass
    board = []
    coordtracker = []
    squaretrackerboard = []
    for i in range(rows):
        board.append([])
        for j in range(columns):
            board[i].append(' ')
    for i in range(rows):
        squaretrackerboard.append([])
        for j in range(columns):
            squaretrackerboard[i].append(' ')
    for i in range(mines):
        row = random.randint(0, rows-1)
        column = random.randint(0, columns-1)
        while [row,column] in coordtracker:
            row = random.randint(0, rows-1)
            column = random.randint(0, columns-1)
        coordtracker.append([row,column])
    for i in range(rows):
        sum = 0
        for j in range(columns):
                if [(i-1),j] in coordtracker:
                    sum += 1
                if [(i-1),(j+1)] in coordtracker:
                    sum += 1
                if [(i+1),j] in coordtracker:
                    sum += 1
                if [(i+1),(j+1)] in coordtracker:
                    sum += 1
                if [i,(j+1)] in coordtracker:
                    sum += 1
                if [i,(j-1)] in coordtracker:
                    sum += 1
                if [(i+1),(j-1)] in coordtracker:
                    sum += 1
                if [(i-1),(j-1)] in coordtracker:
                    sum += 1
                if [i,j] in coordtracker:
                    sum = 0
                else:
                    sum = str(sum)
                    squaretrackerboard[i][j] = sum+''
                    sum = 0
    return [board,coordtracker,rows,columns,squaretrackerboard,mines]
def playing():
    gather = boardcreation()
    board = gather[0]
    coordtracker = gather[1]
    while True:
        count = 0
        for ele in board:
            count += ele.count(' ')
        if count == gather[5]:
            print('You Win')
            userin = input('Would you like to play again Y/N: ')
            if userin.lower() == 'y':
                playing()
            break
        guessrow = int(input('Enter the Row You would Like to guess: '))
        while guessrow == 0 or guessrow >gather[2]+1:
            print('Please Enter a Valid Row')
            guessrow = int(input('Enter the Row You would Like to guess: '))
        guessrow -=1
        guesscolumn = int(input('Enter the Column You would Like to guess: '))
        while guesscolumn == 0 or guesscolumn >gather[3]+1:
            print('Please Enter a Valid Column')
            guesscolumn = int(input('Enter the Column You would Like to guess: '))
        guesscolumn -=1
        if [guessrow,guesscolumn] in coordtracker:
            print('BANGGGGGGG You Lose')
            userin = input('Would you Like to play again Y/N: ')
            if userin.lower() == 'y':
                playing()
            break
        else:
            board[guessrow][guesscolumn] = gather[4][guessrow][guesscolumn]
            for i in range(len(board)):
                print(board[i])
playing()




    
