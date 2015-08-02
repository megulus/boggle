__author__ = 'megdahlgren'

import random
import math


class BoggleDie(object):
    '''
    currently, this method will return instances of dice for game of "New Boggle" (game updated c. 2008)
    '''
    def __init__(self, letters):
        self.letters = letters
        self.face = random.choice(letters)
    @staticmethod
    def all_dice():
        return [BoggleDie(['A','A','E','E','G','N']), BoggleDie(['A','B','B','J','O','O']),
                BoggleDie(['A','C','H','O','P','S']), BoggleDie(['A','F','F','K','P','S']),
                BoggleDie(['A','O','O','T','T','W']), BoggleDie(['C','I','M','O','T','U']),
                BoggleDie(['D','E','I','L','R','X']), BoggleDie(['D','E','L','R','V','Y']),
                BoggleDie(['D','I','S','T','T','Y']), BoggleDie(['E','E','G','H','N','W']),
                BoggleDie(['E','E','I','N','S','U']), BoggleDie(['E','H','R','T','V','W']),
                BoggleDie(['E','I','O','S','S','T']), BoggleDie(['E','L','R','T','T','Y']),
                BoggleDie(['H','I','M','N','U','Qu']), BoggleDie(['H','L','N','N','R','Z'])]


class BoggleBoard(object):
    def __init__(self):
        self.dice = BoggleDie.all_dice()
        random.shuffle(self.dice)
        self.board_dim = int(math.sqrt(len(self.dice)))
        self.board_layout = []
        row = []
        for each_die in range(len(self.dice)):
            if len(row) == self.board_dim:
                self.board_layout.append(row)
                row = []
            row.append(self.dice[each_die])
        self.board_layout.append(row)



    def neighbors(self, x, y):
        self.neighbors = []
        for each_x in range(max(0, x - 1), min(x + 2, self.board_dim)):
            for each_y in range(max(0, y - 1), min(y + 2, self.board_dim)):
                if abs(each_x - x) <= 1 and abs(each_y - y) <= 1:
                    nbr_coords = (each_x, each_y)
                    if (each_x, each_y) != (x, y):
                        self.neighbors.append((each_x, each_y))
        return self.neighbors


    def print_board(self):
        for x in range(self.board_dim):
            row = ''
            for y in range(self.board_dim):
                die = self.board_layout[x][y]
                row = row + '  ' + die.face
            print row



def main():
    board = BoggleBoard()
    board.print_board()
    neighbors = board.neighbors(0,2)
    print neighbors



if __name__ == '__main__':
    main()




