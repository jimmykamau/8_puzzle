import math


def move(state, direction):
    state_copy = list(state)
    board_size = len(state_copy)
    number_of_edges = int(math.sqrt(board_size))
    blank_location = state_copy.index('0')

    if direction == "UP" and blank_location > number_of_edges - 1:
        index_to_swap = blank_location - number_of_edges
    elif direction == "DOWN" and blank_location < board_size - number_of_edges:
        index_to_swap = blank_location + number_of_edges
    elif direction == "LEFT" and blank_location != 0 and (
            (blank_location) % number_of_edges != 0):
        index_to_swap = blank_location - 1
    elif direction == "RIGHT" and (
            (blank_location + 1) % number_of_edges != 0):
        index_to_swap = blank_location + 1
    else:
        return False
    state_copy[blank_location], state_copy[index_to_swap] = \
        state_copy[index_to_swap], state_copy[blank_location]
    return state_copy


def get_child_nodes(node):
    order_of_visits = ["UP", "DOWN", "LEFT", "RIGHT"]
    children = []
    for direction in order_of_visits:
        child = move(node, direction)
        if child:
            children.append(child)
    return children
