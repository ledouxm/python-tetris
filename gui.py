from grid import Grid
from game import Tetris
import tkinter as tk
from utils import colors_by_piece_name

CELL_SIZE = 40
NB_COLUMNS = 10
NB_ROWS = 20
WIDTH = CELL_SIZE * NB_COLUMNS
HEIGHT = CELL_SIZE * NB_ROWS

def draw_cell(canvas, y, x, color="#FCBEDF"):
    x = x * CELL_SIZE
    y = y * CELL_SIZE
    canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=color, outline="white", width="2")


def draw_grid(canvas, grid: Grid):
    # grid = grid.grid
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            draw_cell(canvas, x, y, colors_by_piece_name[grid[x][y]])


game = Tetris(seed='salutàtouss')

def on_click(e):
    game.drop_current_piece()
    draw_grid(canvas, game.draw_current_piece())


win = tk.Tk()

canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.bind('<Button-1>', on_click)
canvas.pack()

game.get_current_piece().snap_to_grid()

draw_grid(canvas, game.draw_current_piece())


win.mainloop()