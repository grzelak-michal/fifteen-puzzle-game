import sys, getopt
import numpy as np
from board import Board

# TODO: implement checking for tile 0 and numbers in rows
def readBoard():
    height = int(input("Insert number of rows: "))
    width = int(input("Insert number of columns: "))

    board = np.zeros((width, height), dtype=int)

    for i in range(height):
        row = list(map(int,input("Insert values for row %d separated by space: " % i).split()))
        board[:][i] = row[:]
    
    return Board(board)



# board = readBoard()
board = Board(np.arange(16).reshape(4, 4))
print(board.is_solved())
board.move('L')
print(board.is_solved())
print(board.board)
print(board.move_history)
