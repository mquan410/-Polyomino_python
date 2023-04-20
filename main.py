# This is a sample Python script.
from coordinate import Coordinate


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from board import Board
from solver import Solver
from pieceLibrary import pieceLibrary


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(6,6)
    solver = Solver(board)
    solver.solve()
    print(solver.isComplete)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
