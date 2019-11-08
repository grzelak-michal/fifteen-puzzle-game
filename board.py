import numpy as np

class Board(object):
    def __init__(self, board):
        self.board = board
        self.blank_position = self.find_blank()
        self.move_history = []
    
    def __getitem__(self, key):
        return self.board[key]
    
    def undo_move(self):
        if len(self.move_history) > 0:
            last_move = self.move_history[-1]
            self.move_history = self.move_history[:-1]

            last_position = tuple(-x for x in Board.get_direction(last_move))

            self._switch_position(last_position)



    def move(self, direction):
        '''Direction is a char LDUR'''
        tuple_direction = Board.get_direction(direction)
        new_position = tuple(map(sum, zip(tuple_direction, self.blank_position)))
        
        if self._is_move_possible(new_position):
            self._switch_position(new_position)

            self.move_history.append(direction)
    
    def _switch_position(self, new_position):
        x1, y1 = new_position
        x2, y2 = self.blank_position
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

        self.blank_position = new_position
    
    def is_solved(self):
        width, height = self.board.shape
        flat_array = self.board.reshape(width * height)
        
        return all(flat_array[i] <= flat_array[i + 1] for i in range(len(flat_array)-1))

    def _is_move_possible(self, new_position):
        width, height = self.board.shape

        if new_position[0] >= 0 and new_position[0] < width and new_position[1] >= 0 and new_position[1] < height:
            return True
        
        return False
    
    def _inversionsCount(self):
        flat_array = self.board.reshape(np.prod(self.board.shape))
        inversions = 0

        for i in range(len(flat_array)):
            for j in range(i + 1, len(flat_array)):
                if flat_array[i] == 0 or flat_array[j] == 0:
                    continue
                
                if flat_array[i] > flat_array[j]:
                    inversions += 1
        
        return inversions

    def find_blank(self):
        width, height = self.board.shape
        for x in range(width):
            for y in range(height):
                if self.board[x][y] == 0:
                    return (x, y)

    @staticmethod  
    def get_direction(dirLetter):
        if dirLetter == 'L':
            return (0, 1)
        elif dirLetter == 'R':
            return (0, -1)
        elif dirLetter == 'U':
            return (1, 0)
        elif dirLetter == 'D':
            return (-1, 0)

    def is_solvable(self):
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
