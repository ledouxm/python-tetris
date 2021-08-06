from random import choice
from game import Tetris

game = Tetris(update=print)
states = game.get_next_states()

state = choice(list(states.values()))

print(state)