from tkinter.constants import ALL, END, LEFT, TRUE, W
from grid import Grid
from game import Tetris
import tkinter as tk
from utils import NB_COLUMNS, NB_ROWS, colors_by_piece_name

CELL_SIZE = 40
WIDTH = CELL_SIZE * NB_COLUMNS
HEIGHT = CELL_SIZE * NB_ROWS

OFFSET_TOP = 30

def draw_cell(canvas: tk.Canvas, y, x, color="#FCBEDF"):
    x = x * CELL_SIZE
    y = y * CELL_SIZE + OFFSET_TOP
    canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=color, outline="white", width="2")


def draw_grid(canvas: tk.Canvas, grid: Grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            draw_cell(canvas, x, y, colors_by_piece_name[grid[x][y]])

def draw_game(canvas: tk.Canvas, game: Tetris):
    canvas.delete(ALL)
    draw_grid(canvas, game.draw_current_piece())
    canvas.create_text(1, OFFSET_TOP / 2, text="score: " + str(game.score), anchor=W)
    

win = tk.Tk()
canvas = tk.Canvas(win, width=WIDTH, height=(HEIGHT + OFFSET_TOP))

def update(game: Tetris):
    canvas.delete(ALL)
    draw_grid(canvas, game.draw_current_piece())

game = Tetris(seed='salutàtouss', update=update)

def on_key_pressed(event):
    if(event.char not in press_events_map): return
    # canvas.delete(ALL)

    press_events_map[event.char]()
    draw_game(canvas, game)

def on_key_released(event):
    if(event.char not in release_events_map): return

    press_events_map[event.char]()
    draw_game(canvas, game)


press_events_map = {
    "q": game.go_left,
    "d": game.go_right,
    "e": game.rotate_clockwise,
    "a": game.rotate_counter_clockwise,
    "s": game.start_soft_drop,
    " ": game.drop_current_piece
}

release_events_map = {
    "s": game.stop_soft_drop()
}

win.bind('<KeyPress>', on_key_pressed)
win.bind('<KeyRelease>', on_key_released)

canvas.pack()


game.get_current_piece().snap_to_grid()

draw_grid(canvas, game.draw_current_piece())


win.mainloop()
