#!/usr/bin/python3
from random import randint
from copy import deepcopy
import sys


class Board:
    """" This class manages the game board """
    BOARD_LENGTH = 4
    BOARD_WIDTH = 4

    def __init__(self, new_board=None):
        if new_board is None:
            row = [0 for x in range(self.BOARD_WIDTH)]
            self.board = [deepcopy(row) for y in range(self.BOARD_LENGTH)]
        else:
            self.board = deepcopy(new_board)

    def print_board(self):
        for row in self.board:
            print(row, file=sys.stderr)

    # Edit the board
    def shift_board(self, direction):
        self.print_board()
        if direction == 'U':  # Up
            print("Shift up", file=sys.stderr)
            for x in range(self.BOARD_WIDTH):
                filled = 0
                for y in range(self.BOARD_LENGTH):
                    if self.board[y][x] is 0:
                        continue
                    if y is 0:
                        if self.board[y][x] is not 0 and self.board[y+1][x] is 0 and self.board[y+2][x] is 0\
                                and self.board[y+3][x] is not 0:
                            if self.board[y][x][0] is self.board[y+3][x][0]\
                                    and self.board[y][x][1] is self.board[y+3][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y+3][x] = 0
                                filled += 1
                                continue
                            elif self.board[y][x][0] is self.board[y+3][x][0]:
                                self.board[y][x] = 0
                                self.board[y+3][x] = 0
                                continue
                    if y + 2 < len(self.board):
                        if self.board[y][x] is not 0 and self.board[y+1][x] is 0 and self.board[y+2][x] is not 0:
                            if self.board[y][x][0] is self.board[y+2][x][0]\
                                    and self.board[y][x][1] is self.board[y+2][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y+2][x] = 0
                                filled += 1
                                continue
                            elif self.board[y][x][0] is self.board[y+2][x][0]:
                                self.board[y][x] = 0
                                self.board[y+2][x] = 0
                                continue
                    if y + 1 < len(self.board):
                        if self.board[y][x] is not 0 and self.board[y+1][x] is not 0:
                            if self.board[y][x][0] is self.board[y+1][x][0]\
                                    and self.board[y][x][1] is self.board[y+1][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y+1][x] = 0
                                filled += 1
                                continue
                            elif self.board[y][x][0] is self.board[y+1][x][0]:
                                self.board[y][x] = 0
                                self.board[y+1][x] = 0
                                continue
                    if self.board[y][x] is not 0:
                        if y is filled:
                            filled += 1
                        else:
                            self.board[filled][x] = self.board[y][x]
                            self.board[y][x] = 0
                            filled += 1
        elif direction == 'R':  # Right
            print("Shift right", file=sys.stderr)
            for y in range(self.BOARD_LENGTH):
                x = len(self.board[y]) - 1
                filled = 3
                if self.board[y][x] is not 0 and self.board[y][x-1] is 0\
                        and self.board[y][x-2] is 0 and self.board[y][x-3] is not 0:
                    if self.board[y][x][0] is self.board[y][x-3][0] and self.board[y][x][1] is self.board[y][x-3][1]:
                        self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                        if x is not filled:
                            self.board[y][x] = 0
                        self.board[y][x-3] = 0
                        continue
                    elif self.board[y][x][0] is self.board[y][x-3][0]:
                        self.board[y][x] = 0
                        self.board[y][x-3] = 0
                        continue
                for tmp_x in range(self.BOARD_WIDTH, 0, -1):
                    x = tmp_x - 1
                    if self.board[y][x] is 0:
                        continue
                    if x-2 > -1:
                        if self.board[y][x] is not 0 and self.board[y][x-1] is 0 and self.board[y][x-2] is not 0:
                            if self.board[y][x][0] is self.board[y][x-2][0]\
                                    and self.board[y][x][1] is self.board[y][x-2][1]:
                                self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if x is not filled:
                                    self.board[y][x] = 0
                                self.board[y][x-2] = 0
                                filled -= 1
                                continue
                            elif self.board[y][x][0] is self.board[y][x-2][0]:
                                self.board[y][x] = 0
                                self.board[y][x-2] = 0
                                continue
                    if x-1 > -1:
                        if self.board[y][x] is not 0 and self.board[y][x-1] is not 0:
                            if self.board[y][x][0] is self.board[y][x-1][0]\
                                    and self.board[y][x][1] is self.board[y][x-1][1]:
                                self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if x is not filled:
                                    self.board[y][x] = 0
                                self.board[y][x-1] = 0
                                filled -= 1
                                continue
                            elif self.board[y][x][0] is self.board[y][x-1][0]:
                                self.board[y][x] = 0
                                self.board[y][x-1] = 0
                                continue
                    if self.board[y][x] is not 0:
                        if x is filled:
                            filled -= 1
                        else:
                            self.board[y][filled] = self.board[y][x]
                            self.board[y][x] = 0
                            filled -= 1
        elif direction == 'L':  # Left
            print("Shift left", file=sys.stderr)
            for y in range(self.BOARD_LENGTH):
                x = 0
                filled = 0
                if self.board[y][x] is not 0 and self.board[y][x+1] is 0\
                        and self.board[y][x+2] is 0 and self.board[y][x+3] is not 0:
                    if self.board[y][x][0] is self.board[y][x+3][0] and self.board[y][x][1] is self.board[y][x+3][1]:
                        self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                        if x is not filled:
                            self.board[y][x] = 0
                        self.board[y][x+3] = 0
                        continue
                    elif self.board[y][x][0] is self.board[y][x+3][0]:
                        self.board[y][x] = 0
                        self.board[y][x+3] = 0
                        continue
                for x in range(self.BOARD_WIDTH):
                    if self.board[y][x] is 0:
                        continue
                    if x+2 < len(self.board[y]):
                        if self.board[y][x] is not 0 and self.board[y][x+1] is 0 and self.board[y][x+2] is not 0:
                            if self.board[y][x][0] is self.board[y][x+2][0]\
                                    and self.board[y][x][1] is self.board[y][x+2][1]:
                                self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if x is not filled:
                                    self.board[y][x] = 0
                                self.board[y][x+2] = 0
                                filled += 1
                                continue
                            elif self.board[y][x][0] is self.board[y][x+2][0]:
                                self.board[y][x] = 0
                                self.board[y][x+2] = 0
                                continue
                    if x+1 < len(self.board[y]):
                        if self.board[y][x] is not 0 and self.board[y][x+1] is not 0:
                            if self.board[y][x][0] is self.board[y][x+1][0]\
                                    and self.board[y][x][1] is self.board[y][x+1][1]:
                                self.board[y][filled] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if x is not filled:
                                    self.board[y][x] = 0
                                self.board[y][x+1] = 0
                                filled += 1
                                continue
                            elif self.board[y][x][0] is self.board[y][x+1][0]:
                                self.board[y][x] = 0
                                self.board[y][x+1] = 0
                                continue
                    if self.board[y][x] is not 0:
                        if x is filled:
                            filled += 1
                        else:
                            self.board[y][filled] = self.board[y][x]
                            self.board[y][x] = 0
                            filled += 1
        elif direction == 'D':  # Down
            print("Shift down", file=sys.stderr)
            for x in range(self.BOARD_WIDTH):
                filled = 3
                for tmp_y in range(self.BOARD_LENGTH, 0, -1):
                    y = tmp_y - 1
                    if self.board[y][x] is 0:
                        continue
                    if y is 3:
                        if self.board[y][x] is not 0 and self.board[y-1][x] is 0\
                                and self.board[y-2][x] is 0 and self.board[y-3][x] is not 0:
                            if self.board[y][x][0] is self.board[y-3][x][0]\
                                    and self.board[y][x][1] is self.board[y-3][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y-3][x] = 0
                                filled -= 1
                                continue
                            elif self.board[y][x][0] is self.board[y-3][x][0]:
                                self.board[y][x] = 0
                                self.board[y-3][x] = 0
                                continue
                    if y - 2 > -1:
                        if self.board[y][x] is not 0 and self.board[y-1][x] is 0 and self.board[y-2][x] is not 0:
                            if self.board[y][x][0] is self.board[y-2][x][0]\
                                    and self.board[y][x][1] is self.board[y-2][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y-2][x] = 0
                                filled -= 1
                                continue
                            elif self.board[y][x][0] is self.board[y-2][x][0]:
                                self.board[y][x] = 0
                                self.board[y-2][x] = 0
                                continue
                    if y - 1 > -1:
                        if self.board[y][x] is not 0 and self.board[y-1][x] is not 0:
                            if self.board[y][x][0] is self.board[y-1][x][0]\
                                    and self.board[y][x][1] is self.board[y-1][x][1]:
                                self.board[filled][x] = [self.board[y][x][0]*3, self.board[y][x][1]]
                                if y is not filled:
                                    self.board[y][x] = 0
                                self.board[y-1][x] = 0
                                filled -= 1
                                continue
                            elif self.board[y][x][0] is self.board[y-1][x][0]:
                                self.board[y][x] = 0
                                self.board[y-1][x] = 0
                                continue
                    if self.board[y][x] is not 0:
                        if y is filled:
                            filled -= 1
                        else:
                            self.board[filled][x] = self.board[y][x]
                            self.board[y][x] = 0
                            filled -= 1
        self.print_board()

    def set_blue(self, location):
        self.board[location[0]-1][location[1]-1] = [1, "blue"]

    def set_red(self, location):
        self.board[location[0]-1][location[1]-1] = [1, "red"]

    # Misc
    def is_filled(self, y, x):
        return self.board[y][x] is not 0

    def is_free_space(self, y, x):
        if y is 0:
            if x is 0:
                return self.board[y+1][x] is 0 or self.board[y][x+1] is 0
            elif x is 3:
                return self.board[y+1][x] is 0 or self.board[y][x-1] is 0
        elif y is 3:
            if x is 0:
                return self.board[y-1][x] is 0 or self.board[y][x+1] is 0
            elif x is 3:
                return self.board[y-1][x] is 0 or self.board[y][x-1] is 0
        else:
            if x is 0:
                return self.board[y-1][x] is 0 or self.board[y+1][x] is 0 or self.board[y][x+1] is 0
            elif x is 3:
                return self.board[y-1][x] is 0 or self.board[y+1][x] is 0 or self.board[y][x-1] is 0
            else:
                return self.board[y-1][x] is 0 or self.board[y+1][x] is 0\
                       or self.board[y][x-1] is 0 or self.board[y][x+1] is 0

    # Check if the whole board can be emptied when placing on specific position
    def is_4_point_board(self, future_turn, blue):
        filled_tiles = self.calc_filled_tiles()
        if filled_tiles is 3:
            tmp_board = Board(new_board=self.board)
            tmp_board.set_blue(future_turn) if blue else tmp_board.set_red(future_turn)
            for direction in ['D', 'R', 'U', 'L']:
                tmp_board.shift_board(direction)
                if tmp_board.calc_filled_tiles() is not 0:
                    return False
            return True
        return False

    def find_free_space(self, y, x):
        if y is 0:
            if self.board[y+1][x] is 0:
                return [y+1, x]
            if x is 0 and self.board[y][x+1]:
                return [y, x+1]
            elif x is 3 and self.board[y][x-1] is 0:
                return [y, x-1]
        elif y is 3:
            if self.board[y-1][x] is 0:
                return [y-1, x]
            if x is 0 and self.board[y][x+1]:
                return [y, x+1]
            elif x is 3 and self.board[y][x-1] is 0:
                return [y, x-1]
        else:
            if x is not 3 and self.board[y][x+1] is 0:
                return [y, x+1]
            elif self.board[y+1][x] is 0:
                return [y+1, x]
            elif x is not 0 and self.board[y][x-1] is 0:
                return [y, x-1]
            elif self.board[y-1][x] is 0:
                return [y-1, x]

    def find_blue_tile_with_space(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] is not 0:
                    if self.board[y][x][1] is "blue" and self.board[y][x][0] is 1 and self.is_free_space(y, x):
                        return self.find_free_space(y, x)
        return None

    def find_red_tile_with_space(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] is not 0:
                    if self.board[y][x][1] is "red" and self.board[y][x][0] is 1 and self.is_free_space(y, x):
                        return self.find_free_space(y, x)
        return None

    # Calculate stuff
    def calc_score(self):
        score = 0
        for y in self.board:
            for x in y:
                if x is not 0:
                    score += x[0]
        return score

    def calc_filled_tiles(self):
        filled_tiles = 0
        for y in self.board:
            for x in y:
                if x is not 0:
                    filled_tiles += 1
        return filled_tiles

    def calc_free_tiles(self):
        return 16 - self.calc_filled_tiles()

    def block_4_points(self):
        filled_tiles = self.calc_filled_tiles()
        if filled_tiles is 2:
            for y in range(self.BOARD_LENGTH):
                if self.board[y][0] is 0 and self.board[y][1] is 0 and self.board[y][2] is 0 and self.board[y][3] is 0:
                    continue
                for x in range(self.BOARD_WIDTH):
                    if self.board[y][x] is 0:
                        continue
                    else:
                        row = deepcopy(self.board[y][x:self.BOARD_WIDTH])
                        column = [self.board[i][x] for i in range(y, self.BOARD_LENGTH)]
                        print(y, x, file=sys.stderr)
                        print(row, file=sys.stderr)
                        print(column, file=sys.stderr)
                        if len(row) > 2:
                            if row[2] is not 0:
                                return [y + 1, x + 3]
                            elif len(row) is 4 and row[3] is not 0:
                                return [y + 1, x + 4]
                        elif len(column) > 2:
                            if column[2] is not 0:
                                return [y + 3, x + 1]
                            elif len(column) is 4 and column[3] is not 0:
                                return [y + 4, x + 1]
        return None

    # Calculate a score based on the total tiles filled and the total score on the board
    def calc_board_score(self):
        filled_tiles = 0
        score = 0
        for y in self.board:
            for x in y:
                if x is not 0:
                    score += x[0]
                    filled_tiles += 1
        free_tiles = 16 - filled_tiles
        if filled_tiles is 0:
            return 0
        elif free_tiles <= 4:
            return free_tiles / 10
        else:
            return score / filled_tiles


board = Board()
# Turns logic
# 0    Set blue
# 1    Set red
# 2    Set red
# 3    Set blue
# 4    Shift board
# 5    Shift board
turn = 0
enemy_turn = None
player = input()


# TODO: Improve functions for calculating best turn (AI)
# Calculate the best place to put a blue tile
def calc_blue():
    filled_tiles = board.calc_filled_tiles()
    if filled_tiles < 2:
        a = randint(1, 4)
        b = randint(1, 4)
        while board.is_filled(a-1, b-1) or board.is_4_point_board([a, b], True):
            a = randint(1, 4)
            b = randint(1, 4)
        
        board.set_blue([a, b])
        print(str(a) + str(b))
        return
    elif filled_tiles is 2:
        block_4_points = board.block_4_points()
        if block_4_points is not None and not board.is_filled(block_4_points[0] - 1, block_4_points[1] - 1):
            board.set_blue(block_4_points)
            print(str(block_4_points[0]) + str(block_4_points[1]))
    elif filled_tiles > 11:
        free_space = board.find_red_tile_with_space()
        if free_space is not None:
            free_space[0] += 1
            free_space[1] += 1
            board.set_blue([free_space[0], free_space[1]])
            print(str(free_space[0]) + str(free_space[1]))
            return
    else:
        free_space = board.find_blue_tile_with_space()
        if free_space is not None:
            free_space[0] += 1
            free_space[1] += 1
            if not board.is_4_point_board([free_space[0], free_space[1]], True):
                board.set_blue([free_space[0], free_space[1]])
                print(str(free_space[0]) + str(free_space[1]))
                return
    a = randint(1, 4)
    b = randint(1, 4)
    while board.is_filled(a-1, b-1) or board.is_4_point_board([a, b], True):
        a = randint(1, 4)
        b = randint(1, 4)

    board.set_blue([a, b])
    print(str(a) + str(b))


# Calculate the best place to put a red tile
def calc_red():
    filled_tiles = board.calc_filled_tiles()
    if filled_tiles < 2:
        a = randint(1, 4)
        b = randint(1, 4)
        while board.is_filled(a-1, b-1) or board.is_4_point_board([a, b], False):
            a = randint(1, 4)
            b = randint(1, 4)    
        
        board.set_red([a, b])
        print(str(a) + str(b))
        return
    elif filled_tiles is 2:
        block_4_points = board.block_4_points()
        if block_4_points is not None and not board.is_filled(block_4_points[0] - 1, block_4_points[1] - 1):
            board.set_red(block_4_points)
            print(str(block_4_points[0]) + str(block_4_points[1]))
    elif filled_tiles > 11:
        free_space = board.find_blue_tile_with_space()
        if free_space is not None:
            free_space[0] += 1
            free_space[1] += 1
            board.set_red([free_space[0], free_space[1]])
            print(str(free_space[0]) + str(free_space[1]))
            return
    else:
        free_space = board.find_red_tile_with_space()
        if free_space is not None:
            free_space[0] += 1
            free_space[1] += 1
            if not board.is_4_point_board([free_space[0], free_space[1]], False):
                board.set_red([free_space[0], free_space[1]])
                print(str(free_space[0]) + str(free_space[1]))
                return
    a = randint(1, 4)
    b = randint(1, 4)
    while board.is_filled(a-1, b-1) or board.is_4_point_board([a, b], False):
        a = randint(1, 4)
        b = randint(1, 4)

    board.set_red([a, b])
    print(str(a) + str(b))


def calc_shift():
    best_score = None
    best_move = None
    moves = ['D', 'R', 'U', 'L']
    possible_moves = ['D', 'R', 'U', 'L']

    for move in moves:
        tmp_board = Board(new_board=board.board)
        print("Shift tmp_board " + move, file=sys.stderr)
        tmp_board.shift_board(move)

        board_score = tmp_board.calc_board_score()
        if tmp_board.board == board.board or tmp_board.calc_filled_tiles() is 0:
            possible_moves.remove(move)
            print("move not possible", file=sys.stderr)
        elif best_score is None or board_score > best_score:
            best_score = board_score
            best_move = move

    if len(possible_moves) is 0:
        print("No possible moves", file=sys.stderr)
        move = moves[randint(0, len(moves) - 1)]
        board.shift_board(move)
        print(move)
    elif best_score is None:
        print("No best move", file=sys.stderr)
        move = possible_moves[randint(0, len(moves) - 1)]
        print("Shift normal board", file=sys.stderr)
        board.shift_board(move)
        print(move)
    else:
        print("Shift normal board", file=sys.stderr)
        board.shift_board(best_move)
        print(best_move)

# Handle the inputs
if player == 'A':
    print("Player A", file=sys.stderr)
    while True:
        if turn % 6 == 0:
            if board.calc_free_tiles() is 0:
                break
            calc_blue()
        elif turn % 6 == 2:
            if board.calc_free_tiles() is 0:
                break
            calc_red()
        elif turn % 6 == 4:
            calc_shift()
        turn += 1
        # Turn done wait for next input
        enemy_turn = input()
        if enemy_turn in ['Quit', 'quit', '']:
            print("Score: " + str(board.calc_score()), file=sys.stderr)
            print("Quitting", file=sys.stderr)
            break
        # Handle enemy turn
        print("Enemy turn: " + enemy_turn, file=sys.stderr)
        if turn % 6 == 1:
            board.set_red([int(x) for x in enemy_turn])
        elif turn % 6 == 3:
            board.set_blue([int(x) for x in enemy_turn])
        elif turn % 6 == 5:
            board.shift_board(enemy_turn)
        turn += 1
        # Go to own turn (top)
elif player == 'B':
    print("Player B", file=sys.stderr)
    while True:
        # Wait for enemy turn
        enemy_turn = input()
        if enemy_turn in ['Quit', 'quit', '']:
            print("Score: " + str(board.calc_score()), file=sys.stderr)
            print("Quitting", file=sys.stderr)
            break
        # Handle enemy turn
        print("Enemy turn: " + enemy_turn, file=sys.stderr)
        if turn % 6 == 0:
            board.set_blue([int(x) for x in enemy_turn])
        elif turn % 6 == 2:
            board.set_red([int(x) for x in enemy_turn])
        elif turn % 6 == 4:
            board.shift_board(enemy_turn)
        turn += 1
        # Go to own turn
        if turn % 6 == 1:
            if board.calc_free_tiles() is 0:
                break
            calc_red()
        elif turn % 6 == 3:
            if board.calc_free_tiles() is 0:
                break
            calc_blue()
        elif turn % 6 == 5:
            calc_shift()
        turn += 1
