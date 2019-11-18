import sys, getopt
import numpy as np
from board import Board, MoveOrder
import algorithms
import time
import heuristics
from copy import deepcopy
import typing
from viewer import Game

# TODO: implement checking for tile 0 and numbers in rows
def readBoard():
    height = int(input("Insert number of rows: "))
    width = int(input("Insert number of columns: "))
    size = height*width

    board = np.zeros((width, height), dtype=int)


    for i in range(width):
        row = list(map(int,input("Insert values for row %d separated by space: " % i).split()))
        if len(row) != height:
            return None
        board[:][i] = row[:]

    temp = board.reshape(size)
    temp = np.sort(temp)
    
    for i in range(size):
        if temp[i] != i:
            return None
    return Board(board)


def programLauncher():
    # sys.argv[0] -> name of the program
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print("~~~~~~~~~~~~~~~~~~")
        print("AVAILABLE COMMANDS")
        print("~~~~~~~~~~~~~~~~~~")
        print("--help order -> List of available commands")
        print("-b order mode / --bfs order mode -> Breadth-first search")
        print("-d order mode / --dfs order mode -> Depth-first search")
        print("-i order mode / --iddfs order mode -> Iterative deepenening DFS")
        print("-h id_of_heuristic mode / --bf id_of_heuristic mode -> Best-first strategy")
        print("-a id_of_heuristic mode / --astar id_of_heuristic mode -> A* strategy")
        print("-s id_of_heuristic mode / --sma id_of_heuristic mode -> SMA* strategy")

        print("~~~~~")
        print("ORDER")
        print("~~~~~")
        print("The order should contain four letters, without any repetitions:")
        print("L -> Left")
        print("R -> Right")
        print("U -> Up")
        print("D -> Down")
        print("Examples: DURL UDLR LURD")
        print("If R is first, then the order will be random for each step.")

        print("~~~~~~~~~~")
        print("HEURISTICS")
        print("~~~~~~~~~~")
        print("There are four different heuristics available:")
        print("h0 -> h(x) = 0, every board has the same value.")
        print("h1 -> Number of inversions in a given board.")
        print("h2 -> Number of misplaced tiles in a given board.")
        print("h3 -> Sum of Manhattan distances in a given board.")

        print("~~~~~")
        print("MODES")
        print("~~~~~")
        print("There are two modes available:")
        print("console -> show moves required to solve the board in console")
        print("viewer -> show solution step by step in GUI")
        exit()

    elif len(sys.argv) != 4:
        print("Wrong number of arguments. Check --help for help.")
        exit()

    else:
        algorithm = None
        argument = None

        if sys.argv[1] == "-b" or sys.argv[1] == "--bfs":
            algorithm = algorithms.BFS
            argument = orderFactory(sys.argv[2])
        elif sys.argv[1] == "-d" or sys.argv[1] == "--dfs":
            algorithm = algorithms.DFS
            argument = orderFactory(sys.argv[2])
        elif sys.argv[1] == "-i" or sys.argv[1] == "--iddfs":
            algorithm = algorithms.IDDFS
            argument = orderFactory(sys.argv[2])
        elif sys.argv[1] == "-h" or sys.argv[1] == "--bf":
            algorithm = algorithms.best_first_search
            argument = heuristicFactory(sys.argv[2])
        elif sys.argv[1] == "-a" or sys.argv[1] == "--astar":
            algorithm = algorithms.A_star
            argument = heuristicFactory(sys.argv[2])
        elif sys.argv[1] == "-s" or sys.argv[1] == "--sma":
            algorithm = algorithms.SMA_star
            argument = heuristicFactory(sys.argv[2])
        else:
            print("Error: Invalid algorithm name. Check --help for help.")
            exit()

        if argument == None:
            print("Error: Invalid second argument. Check --help for help.")
            exit()

        if not (sys.argv[3] == "console" or sys.argv[3] == "viewer"):
            print("Error: Invalid viewing mode. Check --help for help.")
            exit()

        board = readBoard()

        if board == None:
            print("Error: Invalid board. Check --help for help.")
            exit()

        if board.is_solvable():
            start = time.time()
            solved = algorithm(board, argument)
            end = time.time()

            if sys.argv[3] == "console":
                print("Found solution in {} moves, time: {}".format(len(solved.move_history), end - start))
                print(solved.move_history)
                exit()

            else:
                game = Game(solved, board.board).show()
                exit()

        else:
            print("Sorry, the board cannot be solved.")


def orderFactory(text):
    if text.count("U") != 1 or text.count("L") != 1 or text.count("D") != 1 or text.count("R") != 1 or len(text) != 4:
        return None
    else:
        return list(text)

def heuristicFactory(text):
    if text == "h0":
        return heuristics.h0
    elif text == "h1":
        return heuristics.h1
    elif text == "h2":
        return heuristics.h2
    elif text == "h3":
        return heuristics.h3
    else:
        return None

programLauncher()
# # board = readBoard()
# arr = np.arange(16)
# # np.random.shuffle(arr)
# board = Board(arr.reshape(4, 4))
# board.move('L')
# board.move('L')
# board.move('L')
# board.move('U')
# board.move('U')
# board.move('U')
# board.move('R')
# board.move('R')
# board.move('R')
# board.move('D')
# board.move('D')
# board.move('D')
# board.move('L')
# board.move('L')
# board.move_history = []
#
# if board.is_solvable():
#     print(board.board)
#
#     start = time.time()
#
#     solved = algorithms.A_star(board, MoveOrder(['R', 'L', 'D', 'U']), heuristics.h3)
#
#     end = time.time()
#
#     print("Found solution in {} moves, time: {}".format(len(solved.move_history), end - start))
#     print(solved.move_history)
#
#     print(solved.board)
#
#     game = Game(solved, board.board)
#     game.show()

