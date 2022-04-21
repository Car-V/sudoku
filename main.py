# this is the actual file
import random
import numpy

# maybe can make a function for the random.sample

# changing rows and cols to being from 0 to 8 fixed issues,
# but now I need to take into account the 3x3 boxes

sudoku = []
solution = []


def check_box(h, v, check, sub):
    s = numpy.array(sub)
    if (h, v) == (0, 0) or (0, 3) or (0, 6) or (3, 0) or (3, 3) or (3, 6) or (6, 0) or (6, 3) or (6, 6):   # top left
        if check in s[h:h+3][v:v+3]: # or s[h+1][v:v+3] or s[h+2][v:v+3]:
            return False
    elif (h, v) == (0, 1) or (0, 4) or (0, 7) or (3, 1) or (3, 4) or (3, 7) or (6, 1) or (6, 4) or (6, 7):   # top mid
        if check in s[h:h+3][v-1:v+2]: # or s[h+1][v-1:v+2] or s[h+2][v-1:v+2]:
            return False
    elif (h, v) == (0, 2) or (0, 5) or (0, 8) or (3, 2) or (3, 5) or (3, 8) or (6, 2) or (6, 5) or (6, 8):   # top right
        if check in s[h:h+3][v-2:v+1]: # or s[h+1][v-2:v+1] or s[h+2][v-2:v+1]:
            return False
    elif (h, v) == (1, 0) or (1, 3) or (1, 6) or (4, 0) or (4, 3) or (4, 6) or (7, 0) or (7, 3) or (7, 6):   # left mid
        if check in s[h-1:h+2][v:v+3]: # or s[h][v:v+3] or s[h+1][v:v+3]:
            return False
    elif (h, v) == (1, 1) or (1, 4) or (1, 7) or (4, 1) or (4, 4) or (4, 7) or (7, 1) or (7, 4) or (7, 7):   # mid
        if check in s[h-1:h+2][v-1:v+2]: # or s[h][v-1:v+2] or s[h+1][v-1:v+2]:
            return False
    elif (h, v) == (0, 0) or (0, 3) or (0, 6) or (3, 0) or (3, 3) or (3, 6) or (6, 0) or (6, 3) or (6, 6):   # right mid
        if check in s[h-1:h+2][v-2:v+1]: # or s[h+1][v:v+3] or s[h+2][v:v+3]:
            return False
    elif (h, v) == (0, 0) or (0, 3) or (0, 6) or (3, 0) or (3, 3) or (3, 6) or (6, 0) or (6, 3) or (6, 6):   # bottom left
        if check in s[h-2:h+1][v:v+3]: # or s[h+1][v:v+3] or s[h+2][v:v+3]:
            return False
    elif (h, v) == (0, 0) or (0, 3) or (0, 6) or (3, 0) or (3, 3) or (3, 6) or (6, 0) or (6, 3) or (6, 6):   # bottom mid
        if check in s[h-2:h+1][v-1:v+2]: # or s[h+1][v:v+3] or s[h+2][v:v+3]:
            return False
    elif (h, v) == (0, 0) or (0, 3) or (0, 6) or (3, 0) or (3, 3) or (3, 6) or (6, 0) or (6, 3) or (6, 6):   # bottom right
        if check in s[h-2:h+1][v-2:v+1]: # or s[h+1][v:v+3] or s[h+2][v:v+3]:
            return False
    else:
        return True


def allowed(hor, vert, symbol, sud):
    sud = numpy.array(sud)
    if symbol in sud[hor]:
        return False
    if symbol in sud[0:9][vert]:
        return False
    return check_box(hor, vert, symbol, sud)


def solve(c, d, cells, count):
    if c == 9:
        c = 0
        if d + 1 == 9:
            return count + 1
    if cells[c][d] != 0:  # skip filled cells
        return solve(c+1, d, cells, count)
    for x in range(1, 10):
        if allowed(c, d, x, cells) and count < 2:
            cells[c][d] = x
            count = solve(c+1, d, cells, count)
    cells[c][d] = 0  # rest on backtrack
    return count


number_of_solutions = 2
while (number_of_solutions != 1):



    # fixed by using
    # random.sample(range(3), 3) provides a random array with values [0, 1, 2]
    #
    # like with rows and cols being used to make unique vals, these ranges and the operation create unique values for
    # appending to rows from 0 to 8, and do so in such a manner that 3x3 boxes are outlined within the entire board,
    # the board being outlined by the whole of rows and cols ([0 1 2] versus [0 1 2 3 4 5 6 7 8])


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

    segment = []

    for i in rows:
        for j in cols:
            # this returns a value from 1 to 9, all of them random and unique before starting again,
            # and makes it uniquely based on the combination of specific row and specific column (not interchangeable)
            # highest val from just within parenthesis is 17; (9, 8) makes 9 + 6 + 2, versus (8, 9) makes 8 + 0 + 3
            # (8, 5) versus (7, 6) is 8 + 6 + 1 versus 7 + 0 + 2, though their original sums are equal
            val = (i + 3*(j % 3) + j//3) % 9 + 1
            # print(val)
            segment.append(val)
        # print(segment)
        # print()
        sudoku.append(segment)
        segment = []
    # print(sudoku)

    # print()
    # for lin in sudoku:
    #     print(lin)

    # board has now been created; need to extract some values that still allow it to be solved
    # make board look cleaner

    # since sudoku is being changed, need copy for solution
    solution = numpy.copy(sudoku)
    # print()

    # 21 is the minimum number of clues needed for a solution, though there could be multiple solutions
    # unique random values being erased
    for blank_square in random.sample(range(81), 60):
        sudoku[blank_square % 9][blank_square // 9] = 0

    # not necessary but just to see its current state
    # for lin in sudoku:
    #     print('[', end='')
    #     for n in lin:
    #         print(f' {n}', end='')
    #     print(' ]')
    # print()

    number_of_solutions = solve(0, 0, sudoku, 1)


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
# this is assuming that the sudoku we are using has one solution, which we need to confirm
