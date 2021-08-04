from tkinter import Grid
import numpy as np
from utils import NB_ROWS, NB_COLUMNS, distance_from_bounds

base_pieces = np.array([
    {
        "name": "I",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": 0,
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
        "name": "J",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
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
        ],
        "rotation": 0,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": -1,
                "y": 1,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
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
        ],
        "rotation": 0,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
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
                "y": -1,
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
        ],
        "rotation": 0,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 1,
                "y": 0,
            },
        ],
        "rotation": 0,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 2,
                "y": 0,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
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
                "y": -1,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
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
        ],
        "rotation": 90,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 1,
                "y": -1,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": -1,
                "y": -1,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 1,
                "y": -1,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
        ],
        "rotation": 90,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": -2,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": -1,
                "y": -1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 1,
                "y": -1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "Z",
        "cells": [
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -1,
                "y": -1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -1,
                "y": 1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -1,
                "y": -1,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": 0,
                "y": -1,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": -1,
                "y": 0,
            },
        ],
        "rotation": 180,
    },
    {
        "name": "I",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -2,
                "y": 0,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "J",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -1,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "L",
        "cells": [
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": -1,
                "y": -1,
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
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": -1,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "S",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
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
        ],
        "rotation": 270,
    },
    {
        "name": "O",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
            },
            {
                "x": -1,
                "y": 1,
            },
        ],
        "rotation": 270,
    },
    {
        "name": "T",
        "cells": [
            {
                "x": -1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 1,
                "y": 0,
            },
            {
                "x": 0,
                "y": 1,
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

def get_piece_with_random_rotation(piece_name: str, rotation: int):
    for piece in base_pieces:
        if piece["name"] == piece_name and piece["rotation"] == rotation:
            return piece

class Piece:
    base_piece
    rotation: 0
    x = 0
    y = round(NB_COLUMNS / 2)

    def __init__(self, piece):
        self.base_piece = piece

    def get_coordinates(self, x = -1, y = -1):
        coords = []
        if(x == -1): x = self.x
        if(y == -1): y = self.y

        for cell in base_piece["cells"]:
            newX = cell["x"] + x
            newY = cell["y"] + y
            coords.append(np.array([newX, newY]))
        
        return coords

    def snap_to_grid(self):
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

        self.x += vertical
        self.y += horizontal 
