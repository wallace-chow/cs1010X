#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def dragonize (num_points , curve):
    if num_points == 0 :
        return curve
    else :
        c = dragonize (num_points -1, curve)
        return put_in_standard_position (connect_ends (revert(rotate (-pi / 2)(c)) , c))
# test:
draw_connected_scaled(4096, dragonize(12, unit_line))
