import queue
from typing import Iterable, Union, Optional, Tuple, Sequence
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
        key = array_to_string(considered_board.board)

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

class SpecialList(object):
    def __init__(self):
        self.sorted_list = list()
        self.index = -1
    
    def add(self, item: Tuple[float, Board, Optional[Board]]) -> None:
        for i in range(len(self.sorted_list)):
            if self.sorted_list[i][0] > item[0]:
                return self.sorted_list.insert(i, item)
            elif self.sorted_list[i][0] == item[0] and (len(self.sorted_list[i][1].move_history) < len(item[1].move_history)):
                return self.sorted_list.insert(i, item)
        
        self.sorted_list.append(item)
    
    def find(self, board: Board) -> Optional[int]:
        for i in range(len(self.sorted_list)):
            if self.sorted_list[i][1] == board:
                return i

        return None
    
    def find_best_children_score(self, board: Board) -> Optional[float]:
        children = []
        for i in range(len(self.sorted_list)):
            if self.sorted_list[i][2] == board:
                children.append(self.sorted_list[i][0])
        
        if children == []:
            return None
        else:
            return min(children)

    def get(self, index) -> Optional[Tuple[float, Board, Optional[Board]]]:
        return self.sorted_list[index]
    
    def pop(self, index) -> Optional[Tuple[float, Board, Optional[Board]]]:
        return self.sorted_list.pop(index)
    
    def __len__(self) -> int:
        return len(self.sorted_list)
    
    def __iter__(self) -> Iterable[Tuple[float, Board, Optional[Board]]]:
        self.index = -1

        return self
    
    def __next__(self) -> Tuple[float, Board, Optional[Board]]:
        try:
            self.index += 1
            return self.sorted_list[self.index]
        except IndexError:
            raise StopIteration

def SMA_star(board: Board, heuristic: callable, move_order=DEFAULT_MOVE_ORDER, limit: int = 100) -> Optional[Board]:
    def smart_heuristic(board):
        value = len(board.move_history) / 100 + heuristic(board)
        return value
    
    board_list = SpecialList()

    board_list.add((heuristic(board), board, None))
    visited = dict()
    used = 1

    while len(board_list) > 0:
        board_score, considered_board, parent = board_list.get(0)

        key = array_to_string(considered_board.board)
        visited[key] = True

        if considered_board.is_solved():
            return considered_board

        successor = next_successor(considered_board, move_order, visited)
        successor_score = -1.0
        if successor != None:
                successor_score = max((board_score, smart_heuristic(successor)))
        else:
            update_parent(board, move_order, visited, board_list, 0)
            board_list.pop(0)
        
        used += 1

        if used > limit:
            worst_board = board_list.pop(len(board_list) - 1)

        board_list.add((successor_score, successor, board))

    return None

def update_parent(board: Board, move_order: MoveOrder, visited: Sequence[str], board_list: SpecialList, board_index: int):
    successor = next_successor(board, move_order, visited, False)

    if successor != None:
        parent_index = board_list.find(board_list[board_index][2])

        if parent_index != None:
            parent = board_list[parent_index]
            children_best_score = board_list.find_best_children_score(board)
            board_score = board_list[board_index][0]

            if board_score != children_best_score:
                board_tuple = board_list.pop(board_index)
                board_tuple[0] = children_best_score
                board_list.add(board_tuple)

                parent_index = board_list.find(parent)

                update_parent(parent, move_order, visited, board_list, parent_index)


def next_successor(board: Board, move_order: MoveOrder, visited: Sequence[str], visit=True):
    for direction in move_order:
        if board.is_move_possible(direction):
            new_board = np.copy(board.board)
            new_history = board.move_history[:]

            new_board = Board(new_board, new_history)
            new_board.move(direction)
            new_key = array_to_string(new_board.board)

            if visited.get(new_key, False) == False:
                key = array_to_string(board.board)
                if visit == True:
                    visited[key] = True
                return new_board
    
    return None

