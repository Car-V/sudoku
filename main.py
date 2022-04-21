# this is the actual file
import random
import numpy as np


rows = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
cols = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
print(rows, cols)
puzzle = []  # need an array 9x9
#  need to make it so that none of the columns and rows match a number
