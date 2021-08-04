import numpy as np
from grid import Grid
from random import Random, shuffle
from pieces import Piece, possible_rotations, single_pieces, get_piece_with_random_rotation

weight_generator = Random()

def random_weight():
    return weight_generator() * 2 - 1

def get_random_piece(generator: Random, piece):
    random_rotation = generator.choice(possible_rotations)
    random_piece = get_piece_with_random_rotation(piece, random_rotation)

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
    generator: Random
    queue: list
    grid: Grid
    
    def __init__(self, seed):
        self.grid = Grid()
        self.generator = Random()
        self.generator.seed(seed)
        self.queue = make_random_queue(self.generator)

    def get_current_piece(self) -> Piece:
        return self.queue[0]

    def drop_current_piece(self):
        self.grid.apply_piece(self.get_current_piece())

        self.queue = self.queue[1:]
        self.get_current_piece().snap_to_grid()

    def draw_current_piece(self):
        return self.grid.draw_current_piece(self.get_current_piece())
