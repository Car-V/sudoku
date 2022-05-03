import random
import numpy
from interface import Interface
from Sudoku import Sudoku

# Interface determines the difficulty of the board wanted by the user.
inter = Interface()
inter.get_difficulty()

# The default for is_one_solution is set to False.
is_one_solution = False
while is_one_solution is False:
    a = Sudoku(inter)
    if inter.difficulty == 2:
        is_one_solution = a.one_answer
    # Easy boards bypass methods that search for multiple solutions to a
    # board because they have enough clues for a unique solution.
    else:
        is_one_solution = True

print()
a.display('board')
inter.offer_solution(a)

