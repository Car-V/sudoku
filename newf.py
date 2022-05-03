import random
from sudoku import Sudoku


class Test:

    def testclass(self, ar):
        solu = Sudoku(3, 3, board=ar).solve(raising=True)
        print(solu)



