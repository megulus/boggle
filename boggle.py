import random
import math
import multiprocessing
import sys
import os


class BoggleDie(object):

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

class BoggleDictionary(object):
    def __init__(self):
        #self.words = set([])
        self.words = set([])
        try:
            with open('words.txt', 'r') as wordfile:
                lines = wordfile.readlines()
                for line in lines:
                    self.words.add(line.rstrip())
        except IOError:
            print 'Dictionary file not found.'
            sys.exit()


class BoggleGame(object):
    def __init__(self, test_board=False):
        if test_board == True:
            self.board = BoggleBoard(test_board = True)
        else:
            self.board = BoggleBoard()
        self.valid_words = BoggleDictionary().words


    def score_game(self, word_queue, min_word_length=3):
        score = 0
        print 'Words scored:'
        scored_words = set([])
        while not word_queue.empty():
            word = word_queue.get()
            if word not in scored_words:
                if word in self.valid_words:
                    if self.board.has_word(word, self.board.board_coordinates):
                        word_score = len(word) - min_word_length + 1
                        score = score + word_score
                        print word, word_score, 'point(s)'
                        scored_words.add(word)
        return score


    def get_user_input(self, min_word_length, word_queue, fileno):
        '''
        getting user input in separate function so it can run as separate process
        :return: string entered by user
        '''
        sys.stdin = os.fdopen(fileno)
        while True:
            user_input = raw_input('Enter a word: ')
            if len(user_input) >= min_word_length:
                word_queue.put_nowait(user_input)



    def run_game(self, num_seconds=180, min_word_length=3):
        self.board.print_board()
        input_word_queue = multiprocessing.Queue()
        fn = sys.stdin.fileno() # get file descriptor to pass to get_user_input
        p = multiprocessing.Process(target=self.get_user_input, args=(min_word_length, input_word_queue, fn))
        p.start()
        p.join(num_seconds)
        if p.is_alive():
            print "Sorry, time's up!"
            p.terminate()
            p.join()
        score = self.score_game(input_word_queue, min_word_length=3)
        print "Total Score:", score



if __name__ == '__main__':
    game = BoggleGame(test_board=True)
    game.run_game(num_seconds=10)




