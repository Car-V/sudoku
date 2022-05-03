import numpy
import random
import copy


class Sudoku:
    """Class for creating and modifying Sudoku boards"""

    def __init__(self, face):
        """Creates a Sudoku object for the board

        :param face: Interface object with difficulty level for board
        """
        # The abstracts are used for creating the unique values of the solution.
        self.abstract_rows = Sudoku.get_abstract()
        self.abstract_cols = Sudoku.get_abstract()
        # Solution has a filled board. Board has empty spaces.
        self.solution = Sudoku.get_solution(self)
        self.board = Sudoku.get_board(self, face)
        # This states whether the solution is unique and is important for the hard boards.
        self.one_answer = Sudoku.solve(self)

################################################################
# These methods are for creating the boards.

    @staticmethod
    def get_abstract():
        """Creates abstract rows and columns to make board inputs from

        :return: list of random numbers 0 to 8
        """
        abstract = []
        for i in random.sample(range(3), 3):
            for a in random.sample(range(3), 3):
                # This will ensure 3x3 boards of Sudoku are legal, not just the rows and columns.
                abstract.append(3 * a + i)
        return abstract

    def get_solution(self):
        """Creates solution for Sudoku board

        :return: list of lists
        """
        # Segment is a list. Sudoku is a list of lists.
        sudoku = []
        segment = []
        for i in self.abstract_rows:
            for j in self.abstract_cols:
                # The value that goes in a coordinate is determined uniquely by those coordinates to prevent overlap.
                val = (i + 3 * (j % 3) + j // 3) % 9 + 1
                segment.append(val)
            sudoku.append(segment)
            segment = []
        return sudoku

    def get_board(self, face):
        """Creates board iteration with empty spaces to be displayed for solving

        :param face: Interface object with difficulty
        :return: list of lists
        """
        self.board = self.solution
        self.solution = numpy.copy(self.board)
        # Easy puzzles have 35 empty spaces, so they don't need to be checked for a unique solution, generating
        # them faster. Harder puzzles have 60 empty spaces and are checked, making generation slower.
        if face.difficulty == 1:
            n = 35
        else:
            n = 60
        for blank_square in random.sample(range(81), n):
            self.board[blank_square % 9][blank_square // 9] = 0
        return self.board

##############################################################
# These methods check for multiple solutions.

    @staticmethod
    def allowed(hor, vert, symbol, sud):
        """Determines whether a number placement is legal in Sudoku

        :param hor: int for row index
        :param vert: int for column index
        :param symbol: int for number input
        :param sud: list of lists resembling Sudoku
        :return: True if placement is legal, False if placement is illegal
        """
        # These loops check for potential repeats of a number in rows and columns.
        for v in range(9):
            if sud[hor][v] == symbol:
                return False
        for w in range(9):
            if sud[w][vert] == symbol:
                return False
        # This checks for potential repeats of a number in a 3x3 box.
        def_ro = hor - hor % 3
        def_co = vert - vert % 3
        for e in range(3):
            for f in range(3):
                if sud[e + def_ro][f + def_co] == symbol:
                    return False
        return True

    @staticmethod
    def permutation(ma, rr, cc):
        """Solves Sudoku board for a solution

        :param ma: list of lists resembling Sudoku board
        :param rr: int for initial row index
        :param cc: int for initial column index
        :return: True if solution was found, False if solution was not found
        """
        # This is the heart of the recursive backtracking method for seeing if the board can be solved,
        # given the number added to the board in solve().
        if rr == 8 and cc == 9:
            return True
        if cc == 9:
            rr += 1
            cc = 0
        if ma[rr][cc] > 0:
            return Sudoku.permutation(ma, rr, cc + 1)
        for numb in range(1, 10):
            if Sudoku.allowed(rr, cc, numb, ma):
                ma[rr][cc] = numb
                if Sudoku.permutation(ma, rr, cc + 1):
                    return True
            ma[rr][cc] = 0
        return False

    @staticmethod
    def find_blank(box):
        """Looks for coordinates of blank spaces in Sudoku board

        :param box: list of lists resembling Sudoku board
        :return: list of tuples
        """
        blank_pos = []
        for g in range(len(box)):
            for h in range(len(box[0])):
                if box[g][h] == 0:
                    blank_pos.append((g, h))
        # Only 20 spaces need to be checked for whether the board has multiple solutions before
        # the remaining empty squares have to lead to a unique solution (60-35).
        return blank_pos[0:25]

    def solve(self):
        """Determines if there are multiple solutions for a Sudoku board

        :return: True if only one solution, False if multiple solutions
        """
        to_work_with = copy.deepcopy(self.board)
        blank_positions = Sudoku.find_blank(to_work_with)
        count = 0
        # Each of 25 blank coordinates are filled with numbers 1-9, then checked to see if the board
        # can still be solved. If more than 2 numbers per coordinate lead to a solved board, the board
        # does not have a unique solution. If only 1 number works, that number is inputted into the board,
        # and the next coordinate is checked.
        for coordinate in blank_positions:
            for sampling in range(1, 10):
                boxes = to_work_with[:]
                # Keeping track of the number last inputted ensures it can be recalled if it's the only
                # number in that spot that allowed for the board to be solved.
                prev_val = boxes[coordinate[0]][coordinate[1]]
                boxes[coordinate[0]][coordinate[1]] = sampling
                temp = boxes[:]
                # If a solution is found for a number in the current coordinate, the counter is increased.
                if Sudoku.permutation(temp, 0, 0):
                    count += 1
                else:
                    boxes[coordinate[0]][coordinate[1]] = prev_val
                if count > 1:
                    return False
            count = 0
        return True

###############################################################
# These methods are for displaying the boards.

    # Borders are used for customizing the display() method.
    border1 = '||===|===|===||===|===|===||===|===|===||'
    border2 = '||---|---|---||---|---|---||---|---|---||'

    @staticmethod
    def sudoku_row(r):
        """Incorporates numbers from Sudoku board into print display

        :param r: int from list
        :return: string print of line of Sudoku board
        """
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

    def display(self, kind):
        """Displays Sudoku

        :param kind: 'board' or 'solution' for whether Sudoku is solved or not when displayed
        :return: print of formatted Sudoku board from list of lists
        """
        if kind == 'board':
            b = self.board
        elif kind == 'solution':
            b = self.solution
        else:
            raise Exception('Must specify board or solution')
        print(Sudoku.border1)
        for part in b[0:2]:
            Sudoku.sudoku_row(part)
            print(Sudoku.border2)
        Sudoku.sudoku_row(b[2])
        print(Sudoku.border1)
        for part in b[3:5]:
            Sudoku.sudoku_row(part)
            print(Sudoku.border2)
        Sudoku.sudoku_row(b[5])
        print(Sudoku.border1)
        for part in b[6:8]:
            Sudoku.sudoku_row(part)
            print(Sudoku.border2)
        Sudoku.sudoku_row(b[8])
        print(Sudoku.border1)
