import queue
from board import Board
import numpy as np 

def array_to_string(arr):
    shape = arr.shape
    return ','.join(map(str, arr.reshape(shape[0] * shape[1])))

def BFS(board, move_order, limit=10):
    q = queue.Queue()
    q.put(board)
    visited = dict()
    
    while not q.empty():
        q_board = q.get()
        key = array_to_string(q_board.board)

        if len(q_board.move_history) > limit:
            continue

        visited[key] = True

        if q_board.is_solved():
            return q_board
        
        for direction in move_order:
            if q_board.is_move_possible(direction):
                new_board = np.copy(q_board.board)
                new_history = q_board.move_history[:]

                new_board = Board(new_board, new_history)
                new_board.move(direction)
                new_key = array_to_string(new_board.board)
                if visited.get(new_key, False) == False:
                    q.put(new_board)

    return None

def DFS(board, move_order, limit=10):
    stack = list()
    stack.append(board)
    visited = dict()

    while len(stack) > 0:
        stack_board = stack.pop()
        key = array_to_string(stack_board.board)

        if len(stack_board.move_history) > limit:
            continue

        visited[key] = True

        if stack_board.is_solved():
            return stack_board
        
        for direction in reversed(move_order):
            if stack_board.is_move_possible(direction):
                new_board = np.copy(stack_board.board)
                new_history = stack_board.move_history[:]

                new_board = Board(new_board, new_history)
                new_board.move(direction)
                new_key = array_to_string(new_board.board)
                
                if visited.get(new_key, False) == False:
                    stack.append(new_board)
    
    return None

def IDDFS(board, move_order, limit=10):
    for i in range(limit):
        result = DFS(board, move_order, i + 1)

        if result != None:
            return result

