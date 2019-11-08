import queue
from board import Board
import numpy as np 

def array_to_string(arr):
    shape = arr.shape
    return ','.join(map(str, arr.reshape(shape[0] * shape[1])))

def BFS(board, move_order, limit=0):
    q = queue.Queue()
    q.put(board)
    visited = dict()
    
    while not q.empty():
        q_board = q.get()
        key = array_to_string(q_board.board)
        visited[key] = True

        if q_board.is_solved():
            return q_board
        
        for direction in move_order:
            if board.is_move_possible(direction):
                new_board = np.copy(q_board.board)
                new_history = q_board.move_history[:]

                new_board = Board(new_board, new_history)
                new_board.move(direction)
                new_key = array_to_string(new_board.board)
                if visited.get(new_key, False) == False:
                    q.put(new_board)

                if limit > 0 and len(q) > limit:
                    raise MemoryError

    return None