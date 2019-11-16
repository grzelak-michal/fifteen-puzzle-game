import sys, getopt
import numpy as np
from board import Board, MoveOrder
import algorithms
import time
import heuristics
from copy import deepcopy
import typing
from viewer import Game

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
# np.random.shuffle(arr)
board = Board(arr.reshape(4, 4))
board.move('L')
board.move('L')
board.move('L')
board.move('U')
board.move('U')
board.move('U')
board.move('R')
board.move('R')
board.move('R')
board.move('D')
board.move('D')
board.move('D')
board.move('L')
board.move('L')
board.move_history = []
board.initial_board = deepcopy(board.board)

if board.is_solvable():
    print(board.board)

    start = time.time()

    solved = algorithms.A_star(board, MoveOrder(['R', 'L', 'D', 'U']), heuristics.h3)

    end = time.time()

    print("Found solution in {} moves, time: {}".format(len(solved.move_history), end - start))
    print(solved.move_history)

    print(solved.board)

    game = Game(solved, board.initial_board)
    game.show()

