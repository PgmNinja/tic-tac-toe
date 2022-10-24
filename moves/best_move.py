
import random

def get_next_move(curr_position, count):
    next_position = None
    if count == 0:
        next_position = (0,0)
    if count == 2 and curr_position in [(0, 1), (0,2), (1,2), (2,2), (2,1)]:
        next_position = (2, 0)
    if count == 4 and curr_position != (1,0):
        next_position = (1,0)
    if count == 4 and curr_position == (1,0):
        next_position = (2,2)
    if count == 6 and curr_position == (2,1):
        next_position = (1,1)
    if count == 6 and curr_position == (1,1):
        next_position = (2,1)
    if count == 6:
        next_position = random.choice([(2,1), (1,1)])
    return next_position