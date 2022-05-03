

# NOT the actual file
import random
import numpy


sudoku = []
solution = []


# everytime we start a new sudoku to parse, it gets larger
# what is this thing with Nones being printed
# there are values becoming None for some reason???


# creating array of blank space positions
def find_blank(box):
    blank_pos = []
    for g in range(len(box)):
        for h in range(len(box[0])):
            if box[g][h] == 0:
                blank_pos.append((g, h))
    return blank_pos[0:20]

# returns whether or not there is a solution, uses temp


def check(mat, ro, co, nu):
    for v in range(9):
        if mat[ro][v] == nu:
            return False
    for w in range(9):
        if mat[w][co] == nu:
            return False
    def_ro = ro - ro % 3
    def_co = co - co % 3
    for e in range(3):
        for f in range(3):
            if mat[e + def_ro][f + def_co] == nu:
                return False
    return True


def permutation(ma, rr, cc):
    if rr == 8 and cc == 9:
        return True
    if cc == 9:
        rr += 1
        cc = 0
    if ma[rr][cc] > 0:
        return permutation(ma, rr, cc+1)
    for numb in range(1, 10):
        if check(ma, rr, cc, numb):
            ma[rr][cc] = l
            if permutation(ma, rr, cc+1):
                return True
        ma[rr][cc] = 0
    return False


def solve(bo):
    # create an array of tuples of the first 20 empty squares
    blank_positions = find_blank(bo)  # [(1, 0), (4, 5), (6, 3)]
    count = 0
    for coordinate in blank_positions:
        for sampling in range(1, 10):
            boxes = bo[:]
            prev_val = boxes[coordinate[0]][coordinate[1]]
            boxes[coordinate[0]][coordinate[1]] = sampling
            temp = boxes[:]
            if permutation(temp, 0, 0):
                count += 1
            else:
                boxes[coordinate[0]][coordinate[1]] = prev_val
            if count > 1:
                return False
        count = 0
    return True


print('Welcome to Sudoku! You will be given a puzzle to solve with one unique solution. ')
typed = 0
while typed != 1 and typed != 2:
    typed = int(input('Type 1 for an easy Sudoku (generates fast) and 2 for a hard Sudoku (generates slow). '))

is_one_solution = False
while is_one_solution is False:

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

    solution = numpy.copy(sudoku)

    if typed == 1:
        n = 35
    else:
        n = 60

    for blank_square in random.sample(range(81), n):  # 35 instead of 60,
        sudoku[blank_square % 9][blank_square // 9] = 0

    if typed == 2:
        to_work_with = sudoku[:]
        is_one_solution = solve(to_work_with)  # was number_of_solutions = solve(0, 0, sudoku, 1)
    else:
        is_one_solution = True


def sudoku_row(r):
    print('||', end='')
    for value in r[0:3]:
        print(f' {value if value != 0 else " "} |', end='')
    print('|', end='')
    for value in r[3:6]:
        print(f' {value if value != 0 else " "} |', end='')
    print('|', end='')
    for value in r[6:9]:
        print(f' {value if value != 0 else " "} |', end='')
    print('|')


def display(grid):
    print(border1)
    for part in grid[0:2]:
        sudoku_row(part)
        print(border2)
    sudoku_row(grid[2])
    print(border1)
    for part in grid[3:5]:
        sudoku_row(part)
        print(border2)
    sudoku_row(grid[5])
    print(border1)
    for part in grid[6:8]:
        sudoku_row(part)
        print(border2)
    sudoku_row(grid[8])
    print(border1)


border1 = '||===|===|===||===|===|===||===|===|===||'
border2 = '||---|---|---||---|---|---||---|---|---||'

print()
display(sudoku)

print()
com = input('Press \'y\' to see the solution: ')
while com.upper() != 'Y':
    com = input('Press \'y\' to see the solution: ')
print()
display(solution)
