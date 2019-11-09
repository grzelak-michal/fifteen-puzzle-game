from check import Assert, AssertTrue, AssertFalse
from board import Board
import numpy as np


board = Board(np.arange(16).reshape(4, 4))

Assert(board.blank_position).equals((0, 0))
AssertTrue(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertFalse(board.is_move_possible('R'))
AssertFalse(board.is_move_possible('D'))

board.move('L')
Assert(board.blank_position).equals((0, 1))
AssertTrue(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertFalse(board.is_move_possible('D'))

board.move('L')
Assert(board.blank_position).equals((0, 2))
AssertTrue(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertFalse(board.is_move_possible('D'))

board.move('L')
Assert(board.blank_position).equals((0, 3))
AssertFalse(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertFalse(board.is_move_possible('D'))

board.move('U')
Assert(board.blank_position).equals((1, 3))
AssertFalse(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('U')
Assert(board.blank_position).equals((2, 3))
AssertFalse(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('U')
Assert(board.blank_position).equals((3, 3))
AssertFalse(board.is_move_possible('L'))
AssertFalse(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('R')
Assert(board.blank_position).equals((3, 2))
AssertTrue(board.is_move_possible('L'))
AssertFalse(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('R')
Assert(board.blank_position).equals((3, 1))
AssertTrue(board.is_move_possible('L'))
AssertFalse(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('R')
Assert(board.blank_position).equals((3, 0))
AssertTrue(board.is_move_possible('L'))
AssertFalse(board.is_move_possible('U'))
AssertFalse(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('D')
Assert(board.blank_position).equals((2, 0))
AssertTrue(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertFalse(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))

board.move('L')
Assert(board.blank_position).equals((2, 1))
AssertTrue(board.is_move_possible('L'))
AssertTrue(board.is_move_possible('U'))
AssertTrue(board.is_move_possible('R'))
AssertTrue(board.is_move_possible('D'))