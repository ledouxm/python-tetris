
from pieces import Piece
from utils import CURRENT_CELL, EMPTY_CELL, NB_COLUMNS, NB_ROWS, distance_from_bounds, is_empty_or_current, is_out_of_bounds
from copy import deepcopy


def make_line():
    line = []
    for i in range(NB_COLUMNS):
        line.append(EMPTY_CELL)
    return line


def make_grid():
    grid = []
    for i in range(NB_ROWS):
        grid.append(make_line())
    return grid


class Grid:
    def __init__(self, grid = make_grid()):
        self.grid = grid

    def get_max_x(self, piece, x:int, y:int):
        for current_x in range(x, len(self.grid)):
            is_possible = self.is_move_possible(piece=piece, x=current_x, y=y)
            if not is_possible:
                return current_x - 1
        return len(self.grid) - 1

    def is_move_possible(self, piece: Piece, x: int, y: int):
        cells = piece.get_coordinates(x, y)
        for coord in cells:
            h, v = distance_from_bounds(coord[0], coord[1])
            is_out = h != 0 or v != 0

            empty = True
            if(not is_out): empty = is_empty_or_current(self.grid[coord[0]][coord[1]])

            if (is_out and v <= 0) or not empty:
                return False

        return True

    def try_piece(self, piece: Piece, y = None):
        copy = deepcopy(self.grid)
        x = self.get_max_x(piece, piece.x, y)

        if(y != None): piece.y = y
        piece.x = x
        cells = piece.get_coordinates()

        for coord in cells:
            if not is_out_of_bounds(coord[0], coord[1]):
                copy[coord[0]][coord[1]] = piece.base_piece["name"]

        return copy

    def apply_piece_copy(self, piece: Piece, y: int):
        newGrid = self.try_piece(piece, y)
        return newGrid


    def apply_piece(self, piece: Piece):
        newGrid = self.try_piece(piece)

        self.grid = newGrid

    def draw_current_piece(self, piece: Piece):
        copy = deepcopy(self.grid)
        cells = piece.get_coordinates()

        for coord in cells:
            if(not is_out_of_bounds(coord[0], coord[1])):
                copy[coord[0]][coord[1]] = CURRENT_CELL
                
        return copy

    def get_lines_to_clear(self):
        lines_to_clear = []
        for x in range(len(self.grid)):
            is_to_clear = True
            for y in range(len(self.grid[x])):
                if self.grid[x][y] == EMPTY_CELL:
                    is_to_clear = False

            if is_to_clear: lines_to_clear.append(x)

        return lines_to_clear

    def clear_lines(self, lines):
        for line_to_clear in lines:
            self.grid.pop(line_to_clear)
            self.grid.insert(0, make_line())

    def get_peaks(self):
        peaks = []
        while(len(peaks) < NB_COLUMNS):
            x = 0
            while(self.grid[x][len(peaks)] == EMPTY_CELL and x < NB_ROWS - 1):
                x += 1
            peaks.append(x)
        print(peaks)
        return peaks

            



        

