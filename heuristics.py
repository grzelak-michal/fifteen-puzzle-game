import typing
from board import Board
import numpy as np

# always 0 -> all choices are equal
def h0(board):
    '''Always 0 -> all choices are equal'''
    return 0

# return number of inversions
def h1(board: Board):
    '''Return number of inversions'''
    return board._inversionsCount()

# return number of misplaced tiles
def h2(board: Board):
    '''Return number of misplaced tiles'''
    count = 0
    width, height = board.board.shape

    flat_board = board.board.reshape(width * height)

    for i in range(width * height):
        if flat_board[i] != 0 and flat_board[i] != i:
            count += 1
    
    return count

# return total manhattan distance
def h3(board: Board):
    '''Return total manhattan distance'''
    manhattan_sum = 0
    width, height = board.board.shape

    for x in range(width):
      for y in range(height):
        desired_x = board[x][y] // height
        desired_y = board[x][y] % width
        manhattan_sum += abs (x - desired_x) + abs (y - desired_y)
    
    return manhattan_sum