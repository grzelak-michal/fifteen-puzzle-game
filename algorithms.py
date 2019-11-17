import queue
from typing import Iterable, Union, Optional
from board import Board, MoveOrder
import numpy as np 
from sortedcontainers import SortedKeyList

def array_to_string(arr):
    shape = arr.shape
    return ','.join(map(str, arr.reshape(shape[0] * shape[1])))

def BFS(board: Board, move_order: MoveOrder, limit=10) -> Optional[Board]:
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

def DFS(board: Board, move_order: MoveOrder, limit=10) -> Optional[Board]:
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

def IDDFS(board: Board, move_order: MoveOrder, limit=10) -> Optional[Board]:
    for i in range(limit):
        result = DFS(board, move_order, i + 1)

        if result != None:
            return result

DEFAULT_MOVE_ORDER = MoveOrder(['U', 'L', 'D', 'R'])

def best_first_search(board: Board, heuristic: callable, move_order=DEFAULT_MOVE_ORDER) -> Optional[Board]:
    board_list = SortedKeyList(key=heuristic)

    board_list.add(board)
    visited = dict()

    while len(board_list) > 0:
        considered_board = board_list.pop(0)
        # print("Distance: {}".format(heuristic(considered_board)))
        key = array_to_string(considered_board.board)

        # if len(considered_board.move_history) > limit:
        #     continue

        visited[key] = True

        if considered_board.is_solved():
            return considered_board

        for direction in move_order:
            if considered_board.is_move_possible(direction):
                new_board = np.copy(considered_board.board)
                new_history = considered_board.move_history[:]

                new_board = Board(new_board, new_history)
                new_board.move(direction)
                new_key = array_to_string(new_board.board)

                if visited.get(new_key, False) == False:
                    board_list.add(new_board)

    return None

def A_star(board: Board, heuristic: callable, move_order=DEFAULT_MOVE_ORDER) -> Optional[Board]:
    def smart_heuristic(board):
        value = len(board.move_history) / 100 + heuristic(board)
        return value

    board_list = SortedKeyList(key=smart_heuristic)

    board_list.add(board)
    visited = dict()

    while len(board_list) > 0:
        considered_board = board_list.pop(0)
        # print("Distance: {}".format(heuristic(considered_board)))
        key = array_to_string(considered_board.board)

        # if len(considered_board.move_history) > limit:
        #     continue

        visited[key] = True

        if considered_board.is_solved():
            return considered_board

        for direction in move_order:
            if considered_board.is_move_possible(direction):
                new_board = np.copy(considered_board.board)
                new_history = considered_board.move_history[:]

                new_board = Board(new_board, new_history)
                new_board.move(direction)
                new_key = array_to_string(new_board.board)

                if visited.get(new_key, False) == False:
                    board_list.add(new_board)

    return None

def SMA_star(board: Board, heuristic: callable, move_order=DEFAULT_MOVE_ORDER) -> Optional[Board]:
    return None