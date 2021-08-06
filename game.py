from tkinter.constants import S
from utils import NB_COLUMNS
from grid import Grid
from random import Random, shuffle
from pieces import Piece, possible_rotations, single_pieces, get_piece_with_rotation
import time

weight_generator = Random()

def random_weight():
    return weight_generator() * 2 - 1

def get_random_piece(generator: Random, piece):
    random_rotation = generator.choice(possible_rotations)
    random_piece = get_piece_with_rotation(piece, random_rotation)

    return random_piece

def make_random_queue(generator: Random):
    new_queue = []
    shuffledPieces = single_pieces.copy()
    shuffle(shuffledPieces, random=generator.random)
    for piece in shuffledPieces:
        new_queue.append(Piece(piece))

    return new_queue

class Tetris:
    score = 0
    tick_interval = 1000
    generator: Random
    queue: list
    grid: Grid
    status: str
    score: int
    is_soft_dropping = False
    interval = None
    
    def __init__(self, seed = "", update = None):
        self.grid = Grid()
        self.update = update
        self.score = 0
        self.status = "playing"
        self.generator = Random()
        self.generator.seed(seed)
        self.queue = make_random_queue(self.generator)

    def get_current_piece(self) -> Piece:
        return self.queue[0]

    def drop_current_piece(self):
        if(self.status == "lost"): return

        self.grid.apply_piece(self.get_current_piece())

        # new piece
        if(len(self.queue) > 1): self.queue = self.queue[1:]
        else: self.queue = make_random_queue(self.generator)

        lines_to_clear = self.grid.get_lines_to_clear()
        self.score += lines_cleared_scores[len(lines_to_clear)]
        self.grid.clear_lines(lines_to_clear)

        current_piece = self.get_current_piece()
        current_piece.snap_to_grid()

        self.tick_interval -= 10

        if not self.grid.is_move_possible(current_piece, current_piece.x, current_piece.y):
            self.status = "lost"

    def draw_current_piece(self):
        return self.grid.draw_current_piece(self.get_current_piece())

    def go_left(self):
        if(self.status == "lost"): return
        
        current_piece = self.get_current_piece()
        target_y = current_piece.y - 1
        if (self.grid.is_move_possible(current_piece, current_piece.x, target_y)):
            current_piece.y = target_y

    def go_right(self):
        if(self.status == "lost"): return

        current_piece = self.get_current_piece()
        target_y = current_piece.y + 1
        if (self.grid.is_move_possible(current_piece, current_piece.x, target_y)):
            current_piece.y = target_y

    def rotate_clockwise(self):
        if(self.status == "lost"): return

        current_piece = self.get_current_piece()
        current_piece.set_rotation((current_piece.rotation + 90) % 360)

    def rotate_counter_clockwise(self):
        if(self.status == "lost"): return

        current_piece = self.get_current_piece()
        current_piece.set_rotation((current_piece.rotation - 90) % 360)

    def start_soft_drop(self):
        self.is_soft_dropping = True
        # self.interval.cancel()

    def stop_soft_drop(self):
        print("stop")
        self.is_soft_dropping = False

    def get_interval(self):
        if(self.is_soft_dropping): 
            return 50
        return self.tick_interval

    def get_next_states(self):
        states = {}

        current_piece = self.get_current_piece()
        piece_name = current_piece.base_piece["name"]
        if(piece_name == "O"):
            rotations = [0]
        elif(piece_name == "I"):
            rotations = [0, 90]
        else: rotations = [0, 90, 180, 270]

        for rotation in rotations:
            piece = Piece(get_piece_with_rotation(piece_name, rotation))
            min_y = min([coord["y"] for coord in piece.base_piece['cells']])
            max_y = max([coord["y"] for coord in piece.base_piece["cells"]])

        for y in range(-min_y, NB_COLUMNS - max_y):
            self.grid.get_max_x(piece, 0, y)
            new_grid = self.grid.apply_piece_copy(current_piece, y)
            states[(y, rotation)] = new_grid

        return states

            



lines_cleared_scores = {
    0: 0,
    1: 40,
    2: 100,
    3: 300,
    4: 1200
}