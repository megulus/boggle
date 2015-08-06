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
    def all_dice(test_board=False):
        if test_board == True:
            return [BoggleDie(['A']), BoggleDie(['A']),
                BoggleDie(['S']), BoggleDie(['P']),
                BoggleDie(['T']), BoggleDie(['M']),
                BoggleDie(['E']), BoggleDie(['S']),
                BoggleDie(['Y']), BoggleDie(['S']),
                BoggleDie(['N']), BoggleDie(['E']),
                BoggleDie(['I']), BoggleDie(['E']),
                BoggleDie(['Qu']), BoggleDie(['R'])]
        else:
            return [BoggleDie(['A','A','E','E','G','N']), BoggleDie(['A','B','B','J','O','O']),
                BoggleDie(['A','C','H','O','P','S']), BoggleDie(['A','F','F','K','P','S']),
                BoggleDie(['A','O','O','T','T','W']), BoggleDie(['C','I','M','O','T','U']),
                BoggleDie(['D','E','I','L','R','X']), BoggleDie(['D','E','L','R','V','Y']),
                BoggleDie(['D','I','S','T','T','Y']), BoggleDie(['E','E','G','H','N','W']),
                BoggleDie(['E','E','I','N','S','U']), BoggleDie(['E','H','R','T','V','W']),
                BoggleDie(['E','I','O','S','S','T']), BoggleDie(['E','L','R','T','T','Y']),
                BoggleDie(['H','I','M','N','U','Qu']), BoggleDie(['H','L','N','N','R','Z'])]


class BoggleBoard(object):
    def __init__(self, test_board=False):
        if test_board == True:
            self.dice = BoggleDie.all_dice(test_board=True)
        else:
            self.dice = BoggleDie.all_dice()
            random.shuffle(self.dice)
        self.board_dim = int(math.sqrt(len(self.dice)))
        self.board_layout = []
        self.board_coordinates = []
        row = []
        i = 0
        j = 0
        for each_die in range(len(self.dice)):
            if len(row) == self.board_dim:
                self.board_layout.append(row)
                row = []
                i = i + 1
                j = 0
            row.append(self.dice[each_die])
            self.board_coordinates.append((i, j))
            j = j + 1
        self.board_layout.append(row)



    def neighbors(self, x, y):
        neighbors = []
        for each_x in range(max(0, x - 1), min(x + 2, self.board_dim)):
            for each_y in range(max(0, y - 1), min(y + 2, self.board_dim)):
                if abs(each_x - x) <= 1 and abs(each_y - y) <= 1:
                    nbr_coords = (each_x, each_y)
                    if (each_x, each_y) != (x, y):
                        neighbors.append((each_x, each_y))
        return neighbors


    def print_board(self):
        for x in range(self.board_dim):
            row = ''
            for y in range(self.board_dim):
                die = self.board_layout[x][y]
                row = row + '  ' + die.face
            print row


    def get_die(self, x, y):
        return self.board_layout[x][y]


    def has_word(self, word, coord_list):
        squares_crossed = []
        for each_tuple in coord_list:
            if self.has_word_starting_at(word, each_tuple, squares_crossed):
                return True
        '''
        for i in range(self.board_dim):
            for j in range(self.board_dim):
                if self.has_word_starting_at(word, (i, j), squares_crossed):
                    return True
        return False
        '''


    def has_word_starting_at(self, word, start_tile, squares_crossed):
        '''
        :param word: string
        :param start_tile: tuple
        :param squares_crossed: list of tuples
        :return: True or False
        '''
        print word, start_tile, squares_crossed
        if word == '':
            return True
        else:
            word = word.lower()
            face = self.get_die(*start_tile).face.lower()
            if word.startswith(face):
                if start_tile not in squares_crossed:
                    squares_crossed.append(start_tile)
                    word = word.strip(face)
                    neighbors = self.neighbors(*start_tile)
                    for neighbor in neighbors:
                        if self.has_word_starting_at(word, neighbor, squares_crossed):
                            return True
                    squares_crossed.remove(start_tile)
        return False





def main():
    board = BoggleBoard(test_board=True)
    board.print_board()
    if board.has_word('QUESTION', board.board_coordinates):
        print 'Yes'
    else:
        print 'Nem'




if __name__ == '__main__':
    main()




