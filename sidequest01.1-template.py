#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(pic, n):
    if n < 3:
        pass
    x1 = quarter_turn_right (stackn(n, quarter_turn_left (pic)))
    z1 = quarter_turn_right (stackn(n - 2, pic))
    z2 = quarter_turn_right (pic)
    z3 = turn_upside_down (stack_frac(1 / (n - 1), z1, z2))
    z4 = quarter_turn_left (stack_frac (1 / n, turn_upside_down(z1), z3))
    z5 = turn_upside_down (x1)
    y1 = turn_upside_down (stack_frac(1 / (n - 1), z5, z4))
    y2 = stack_frac (1 / n, x1, y1)
    return y2
    
    
    

# Test
show(egyptian(nova_bb, 5))
