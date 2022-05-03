import random
from sudoku import Sudoku
from newf import Test

# puzzle = Sudoku(3).difficulty(0.5)
# puzzle.show()
# solution = puzzle.solve()
# solution.show()

k = [1, 2, 3, 4, 5, 6, 7]
print(k[-3:])


b = [1, 2, 3]
c = b[:]
print(c)

tar = [[8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9],
     [8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9],
     [8, 7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1, 9]]

k = Test.testclass(Test, tar)
print(k)
print('cut off here')
sudoku = []

rows = []
for i in random.sample(range(3), 3):
    for a in random.sample(range(3), 3):
        rows.append(3 * a + i)

cols = []
for j in random.sample(range(3), 3):
    for b in random.sample(range(3), 3):
        cols.append(3 * b + j)

segment = []

for i in rows:
    for j in cols:
        val = (i + 3 * (j % 3) + j // 3) % 9 + 1
        segment.append(val)
    sudoku.append(segment)
    segment = []

for blank_square in random.sample(range(81), 60):  # 35 instead of 60,
    sudoku[blank_square % 9][blank_square // 9] = 0

print(sudoku)


def find_blank(box):
    blank_pos = []
    for g in range(len(box)):
        for h in range(len(box[0])):
            if box[g][h] == 0:
                blank_pos.append((g, h))
    return blank_pos[0:20]


print(find_blank(sudoku))

sudoku[0][0] = 1
sudoku[0][1] = 1
puzzle2 = Sudoku(3, 3, board=sudoku)
print(puzzle2)
solution2 = puzzle2.solve(raising=True)
# print(solution2)

arr = sudoku
sol = Sudoku(3, 3, board=arr).solve(raising=True)
print(sol)
