# this is the actual file
import random
# import numpy as np


# maybe can make a function for the random.sample

# changing rows and cols to being from 0 to 8 fixed issues,
# but now I need to take into account the 3x3 boxes

# fixed by using
# random.sample(range(3), 3) provides a random array with values [0, 1, 2]

# these rows and columns are abstract; segment, made from appended vals, made from a unique combination derived from
# rows and cols, is each actual row, and cols don't have matching nums because of the unique way vals is found by both
# 'rows' and 'cols'
rows = []
for i in random.sample(range(3), 3):
    for a in random.sample(range(3), 3):
        rows.append(3*a + i)
cols = []
for j in random.sample(range(3), 3):
    for b in random.sample(range(3), 3):
        cols.append(3*b + j)

# base = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)

sudoku = []
segment = []

for i in rows:
    for j in cols:
        # this returns a value from 1 to 9, all of them random and unique before starting again,
        # and makes it uniquely based on the combination of specific row and specific column (not interchangeable)
        # highest val from just within parenthesis is 17; (9, 8) makes 9 + 6 + 2, versus (8, 9) makes 8 + 0 + 3
        # (8, 5) versus (7, 6) is 8 + 6 + 1 versus 7 + 0 + 2, though their original sums are equal
        val = (i + 3*(j % 3) + j//3) % 9 + 1
        print(val)
        segment.append(val)
    print(segment)
    print()
    sudoku.append(segment)
    segment = []
print(sudoku)

print()
for lin in sudoku:
    print(lin)

# board has now been created; need to extract some values that still allow it to be solved
# make board look cleaner
