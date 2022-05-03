# Interface calls Sudoku in offer_solution().
from Sudoku import Sudoku


class Interface:
    """How the code interacts with the user"""

    def __init__(self):
        """Initializing the Interface object"""
        # Difficulty is for the type of Sudoku board corresponding to this Interface object.
        self.difficulty = None

    def get_difficulty(self):
        """Welcomes the user and gets type of Sudoku wanted

        :return: Outputs of welcome and prompts for the difficulty input
        """
        print('Welcome to Sudoku! You will be given a puzzle to solve with one unique solution. ')
        self.difficulty = 0
        # Only 1 and 2 are acceptable answers for difficulty.
        while self.difficulty != 1 and self.difficulty != 2:
            self.difficulty = int(input('Type 1 for an easy Sudoku (generates fast) and 2 for a '
                                        'hard Sudoku (generates slow). '))

    @staticmethod
    def offer_solution(s):
        """Offers Sudoku board solution to the user

        :param s: Sudoku object
        :return: prompt for showing solution; board solution
        """
        print()
        # Only 'y' and 'Y' are acceptable answers for seeing the solution.
        com = input('Press \'y\' to see the solution: ')
        while com.upper() != 'Y':
            com = input('Press \'y\' to see the solution: ')
        print()
        # The method ends with calling the Sudoku class for displaying the solution.
        Sudoku.display(s, 'solution')
