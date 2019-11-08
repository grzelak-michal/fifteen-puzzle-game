import sys, getopt
import numpy as np
from board import Board
import algorithms

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
arr = np.arange(16)
np.random.shuffle(arr)
board = Board(arr.reshape(4, 4))
if board.is_solvable():
    print(board.board)
    solved = algorithms.BFS(board, ['L', 'R', 'U', 'D'])
    print(solved.board)

