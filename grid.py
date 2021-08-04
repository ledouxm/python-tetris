
from pieces import Piece
from utils import CURRENT_CELL, EMPTY_CELL, NB_COLUMNS, NB_ROWS, distance_from_bounds, is_empty, is_empty_or_current, is_out_of_bounds, log_grid


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
    grid = make_grid()

    def get_max_x(self, piece: Piece):
        y = piece.y
        for x in range(len(self.grid)):
            is_possible = self.is_move_possible(piece=piece, x=x, y=y)
            if not is_possible:
                return x - 1
        return len(self.grid) - 1

    def is_move_possible(self, piece: Piece, x: int, y: int):
        cells = piece.get_coordinates(x, y)
        for coord in cells:
            h, v = distance_from_bounds(coord[0], coord[1])
            is_out = h != 0 or v != 0

            empty = True
            if(not is_out): empty = is_empty_or_current(self.grid[coord[0]][coord[1]])

            if (is_out and v < 0) or not empty:
                return False

        return True

    def try_piece(self, piece:Piece):
        copy = self.grid.copy()
        x = self.get_max_x(piece)

        piece.x = x
        cells = piece.get_coordinates()
        for coord in cells:
            if not is_out_of_bounds(coord[0], coord[1]):
                copy[coord[0]][coord[1]] = piece.base_piece["name"]

        return copy

    def apply_piece(self, piece: Piece):
        newGrid = self.try_piece(piece)
        self.grid = newGrid

    def draw_current_piece(self, piece: Piece):
        copy = self.grid.copy()
        cells = piece.get_coordinates()
        for coord in cells:
            if(not is_out_of_bounds(coord[0], coord[1])):
                copy[coord[0]][coord[1]] = CURRENT_CELL
        return copy