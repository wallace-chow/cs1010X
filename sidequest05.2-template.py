#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    rotated_left = rotate(pi/3)(kochize(level - 1))
    rotated_right = rotate(-pi/3)(kochize(level - 1))
    first_part = connect_ends (kochize(level - 1), rotated_left)
    second_part = connect_ends (rotated_right, kochize(level - 1))
    last_part = connect_ends(first_part, second_part)
    return put_in_standard_position(last_part)

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    piece = kochize(5)
    left_rotated = rotate(pi/3)(piece)
    right_rotated = rotate(-pi/3)(piece)
    inverted = rotate(pi)(piece)
    step1 = connect_ends(left_rotated, right_rotated)
    step2 = connect_ends(step1, inverted)
    step3 = connect_ends(step2, step2)
    return step3

draw_connected_scaled(10000, snowflake())
