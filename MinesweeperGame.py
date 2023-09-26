#Minesweeper game
import random
def boardcreation():
    rows = int(input('Input the amount of rows you would like to play with (Whole Number): '))
    columns = int(input('Input the amount of columns you would like to play with (Whole Number): '))
    mines = int(input('Input the amount of mines you would like to play with (Whole Number): '))
    board = []
    coordtracker = []
    for i in range(rows):
        board.append([])
        for j in range(columns):
            board[i].append(' ')
    for i in range(mines):
        row = random.randint(0, rows - 1)
        column = random.randint(0, columns - 1)
        while [row,column] in coordtracker:
            row = random.randint(0, rows - 1)
            column = random.randint(0, columns - 1)
        coordtracker.append([row,column])
    return [board, coordtracker]
def playing():
    gather = boardcreation()
    board = gather[0]
    coordtracker = gather[1]
    useralive = True
    while useralive:
        guessrow = int(input('Enter the Row You would Like to guess: '))
        guesscolumn = int(input('Enter the Column You would Like to guess: '))
        if [guessrow,guesscolumn] in coordtracker:
            print('BANGGGGGGG You Lose')
            useralive = False
        else:
            board[guessrow-1][guesscolumn-1] = 'O'
            for i in range(len(board)):
                print(board[i])
playing()


    
