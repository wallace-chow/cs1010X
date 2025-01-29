#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *
########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def julia (x1, y1, depth1, depth2, max_iter = 120):
    translation = 300
    scale = 1000
    c = complex(x1,y1)
    def helper(x, y):
        z = complex ((x-translation)/scale, (y - translation)/scale)
        for i in range (max_iter):
            z = z **2 + c
            if abs(z) > 2:
                return 0
        if z == 2:
            return depth1
        return depth2
    return helper

anaglyph(function_to_painter(julia(-0.54, 0.54, 1, 1)))      
# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
