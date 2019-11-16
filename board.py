import numpy as np
from typing import Sequence, Tuple, Iterable
import random

class Board(object):
    def __init__(self, board: Sequence[Sequence[int]], move_history: Sequence[str] = []):
        self.board = board
        self.blank_position = self.find_blank()
        self.move_history = move_history
    
    def __getitem__(self, key: int) -> Sequence[int]:
        return self.board[key]
    
    def undo_move(self) -> None:
        if len(self.move_history) > 0:
            last_move = self.move_history[-1]
            self.move_history = self.move_history[:-1]
            tuple_direction = tuple(-x for x in Board.get_direction(last_move))
            last_position = tuple(map(sum, zip(tuple_direction, self.blank_position)))

            self._switch_position(last_position)
    
    def direction_to_position(self, direction: str) -> Tuple[int, int]:
        tuple_direction = Board.get_direction(direction)
        new_position = tuple(map(sum, zip(tuple_direction, self.blank_position)))

        return new_position

    def move(self, direction: str) -> bool:
        '''Direction is a char LDUR'''
        
        new_position = self.direction_to_position(direction)

        if self.is_move_possible(direction):
            self._switch_position(new_position)
            self.move_history.append(direction)

            return True
        
        return False
    
    def _switch_position(self, new_position: Tuple[int, int]) -> None:
        x1, y1 = new_position
        x2, y2 = self.blank_position
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

        self.blank_position = new_position
    
    def is_solved(self) -> bool:
        width, height = self.board.shape
        flat_array = self.board.reshape(width * height)
        
        return all(flat_array[i] <= flat_array[i + 1] for i in range(len(flat_array)-1))

    def is_move_possible(self, direction) -> bool:
        new_position = self.direction_to_position(direction)
        width, height = self.board.shape

        if new_position[0] >= 0 and new_position[0] < width and new_position[1] >= 0 and new_position[1] < height:
            return True
        
        return False
    
    def _inversionsCount(self) -> int:
        flat_array = self.board.reshape(np.prod(self.board.shape))
        inversions = 0

        for i in range(len(flat_array)):
            for j in range(i + 1, len(flat_array)):
                if flat_array[i] == 0 or flat_array[j] == 0:
                    continue
                
                if flat_array[i] > flat_array[j]:
                    inversions += 1
        
        return inversions

    def find_blank(self) -> Tuple[int, int]:
        width, height = self.board.shape
        for x in range(width):
            for y in range(height):
                if self.board[x][y] == 0:
                    return (x, y)

    @staticmethod  
    def get_direction(dirLetter) -> Tuple[int, int]:
        if dirLetter == 'L':
            return (0, 1)
        elif dirLetter == 'R':
            return (0, -1)
        elif dirLetter == 'U':
            return (1, 0)
        elif dirLetter == 'D':
            return (-1, 0)

    def is_solvable(self) -> bool:
        inversions = self._inversionsCount()
        width, height = self.board.shape

        if width % 2 == 1 and inversions % 2 == 1:
            return False
        elif width % 2 == 0:
            if height % 2 == 0 and ((inversions + self.blank_position[0]) % 2 != 0):
                return False
            elif height % 2 == 1 and ((inversions + self.blank_position[0]) % 2 != 1):
                return False
        
        return True
