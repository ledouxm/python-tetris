NB_COLUMNS = 10
NB_ROWS = 20

EMPTY_CELL = "*"
CURRENT_CELL = "#"

def is_empty(val: str):
    return val == EMPTY_CELL

def is_empty_or_current(val: str):
    return is_empty(val) or val == CURRENT_CELL

def is_out_of_bounds(x: int,y :int):
    horizontal, vertical = distance_from_bounds(x, y)
    
    return horizontal != 0 or vertical != 0
# const getDistanceFromBounds = (x: number, y: number) => ({
#     vertical: x < 0 ? -x : x >= HEIGHT ? x - HEIGHT - 1 : 0,
#     horizontal: y < 0 ? -y : y >= WIDTH ? -y + (WIDTH - 1) : 0,
# });
def distance_from_bounds(x: int, y :int):
    vertical = 0
    horizontal = 0

    if(x < 0): 
        vertical = -x
    elif(x >= NB_ROWS): vertical = x - NB_ROWS - 1

    if(y < 0): 
        horizontal = -y
    elif(y >= NB_COLUMNS): horizontal = - y + NB_COLUMNS - 1

    return horizontal, vertical

colors_by_piece_name = {
    "I": "#264653",
    "J": "#2a9d8f",
    "L": "#8AB17D",
    "Z": "#BABB74",
    "S": "#E9C46A",
    "O": "#F4A261",
    "T": "#E76F51",
    "*": "white",
    "#": "orange"
}

def log_grid(grid):
    for x in range(len(grid)):
        str = ""
        for y in range(len(grid[x])):
            str+=grid[x][y]

        print(str)