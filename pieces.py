from tkinter import Grid
import numpy as np
from utils import NB_ROWS, NB_COLUMNS, distance_from_bounds

base_pieces = np.array([
    {
        "name": "I",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 1,
                "y": 3,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 0,
                "y": 2,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 0,
                "y": 1,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": 0,
                "y": 2,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 2,
                "y": 2,
            },
            {
                "x": 3,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 2,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 0,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 2,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": 2,
                "y": 0,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 2,
                "y": 2,
            },
            {
                "x": 2,
                "y": 3,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 2,
                "y": 2,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 2,
                "y": 0,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 2,
                "y": 2,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 2,
                "y": 0,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
            {
                "x": 2,
                "y": 1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 3,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 2,
                "y": 0,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 2,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 0,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 2,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 1,
                "y": 2,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 1,
                "y": 1,
            },
            {
                "x": 2,
                "y": 1,
            },
            {
                "x": 1,
                "y": 0,
            },
        ],
        "rotation": 270,
    },
])

single_pieces = []

for base_piece in base_pieces:
    if base_piece["rotation"] == 0:
        single_pieces.append(base_piece)

possible_rotations = [0, 90, 180, 270]

def get_piece_with_rotation(piece_name: str, rotation: int):
    for piece in base_pieces:
        if piece["name"] == piece_name and piece["rotation"] == rotation:
            return piece

class Piece:
    base_piece
    rotation: 0
    x = 3
    y = round(NB_COLUMNS / 2)

    def __init__(self, piece):
        self.base_piece = piece
        self.rotation = piece["rotation"]

    def get_coordinates(self, x = -float('inf'), y = -float('inf')):
        coords = []
        if(x == -float('inf')): x = self.x
        if(y == -float('inf')): y = self.y

        for cell in self.base_piece["cells"]:
            newX = cell["x"] + x
            newY = cell["y"] + y
            coords.append(np.array([newX, newY]))
        
        return coords

    def snap_to_grid(self, only_horizontal = False):
        vertical = 0
        horizontal = 0

        cells = self.get_coordinates()
        for coord in cells:
            currentH, currentV = distance_from_bounds(coord[0], coord[1])
            # if(horizontal == 0): horizontal = currentH
            if(currentH != 0 and abs(currentH - horizontal) >= 0): 
                horizontal = currentH 
            if(currentV != 0 and abs(currentV - vertical) >= 0):
                vertical = currentV

        if(not only_horizontal): self.x += vertical
        print("snapping h", horizontal)
        self.y += horizontal 

    def try_rotation(self, new_rotation):
        if(not new_rotation % 90 == 0): return

        

    def set_rotation(self, new_rotation):
        if(not new_rotation % 90 == 0): return
        
        self.base_piece = get_piece_with_rotation(self.base_piece['name'], new_rotation)
        self.rotation = new_rotation

        self.snap_to_grid(True)
