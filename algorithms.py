import queue
from board import Board
import copy 

def BFS(board, move_order, limit=0):
    q = queue.Queue()
    q.put(board)

    while not q.empty():
        q_board = q.get()

        if q_board.is_solved():
            return q_board
        
        for direction in move_order:
            if board.is_move_possible(direction):
                new_board = copy.deepcopy(q_board)
                new_board.move(direction)

                q.put(new_board)
                print(q.qsize())
                if limit > 0 and len(q) > limit:
                    raise MemoryError

    return None