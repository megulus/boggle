__author__ = 'megdahlgren'

import random
import math
import time
import enchant




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



    def has_word_starting_at(self, word, start_tile, squares_crossed):
        '''
        :param word: string
        :param start_tile: tuple
        :param squares_crossed: list of tuples
        :return: True or False
        '''
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



class BoggleGame(object):
    def __init__(self, test_board=False):
        if test_board == True:
            self.board = BoggleBoard(test_board = True)
        else:
            self.board = BoggleBoard()
        self.user_word_input = set()
        self.valid_words = enchant.Dict('en_US')

    def score_game(self, set_of_words, min_word_length=3):
        score = 0
        print 'Words scored:'
        for word in set_of_words:
            if self.valid_words.check(word):
                if self.board.has_word(word, self.board.board_coordinates):
                    word_score = len(word) - min_word_length + 1
                    score = score + word_score
                    print word, word_score, 'point(s)'
        return score


    def run_game(self, seconds=180, min_word_length=3):
        self.board.print_board()
        time_up = time.time() + seconds
        while time.time() < time_up:
            user_input = raw_input("Enter word (minimum 3 letters): ")
            if len(user_input) >= min_word_length:
                self.user_word_input.add(user_input)
        print "Time up."
        score = self.score_game(self.user_word_input, min_word_length=3)
        print "Total Score:", score



def main():
    game = BoggleGame(test_board=True)
    game.run_game(seconds=60)





if __name__ == '__main__':
    main()




