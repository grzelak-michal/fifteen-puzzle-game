import numpy as np

class Board(object):
    def __init__(self, board):
        self.board = board
    
    def __getitem__(self, key):
        return self.board[key]