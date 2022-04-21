# this is the actual file
import random
import numpy as np


# maybe can make a function for the random.sample
rows = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
cols = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)

base = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)

sudoku = []
segment = []

for i in rows:
    for j in cols:
        # this returns a value from 1 to 9, all of them random and unique before starting again,
        # and makes it uniquely based on the combination of specific row and specific column (not interchangeable)
        val = (i + 3*(j % 3) + j//3) % 9 + 1
        # this will help get a specific index for the array
        # we can combine this with another random vector (base)
        segment.append(val)
    sudoku.append(segment)
    segment = []


# now getting a board that repeats a number in each row, found at the same index in each row
# columns are unique
print(sudoku)
print()
for lin in sudoku:
    print(lin)
# print(rows, cols)
# puzzle = []  # need an array 9x9
#  need to make it so that none of the columns and rows match a number
