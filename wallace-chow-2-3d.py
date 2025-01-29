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

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.

def newton_rap_frac (d1,d2,d3, max_iter = 15):
    epsilon = 10 ** (-7)
    translation = 300
    scale = 200
    def helper(x, y):        
        z1 = complex((x - translation)/scale, (y - translation)/scale)
        r1 = complex(1,0)
        r2 = complex(-1/2, sqrt(3)/2)
        r3 = complex (-1/2, -sqrt(3)/2)
        a = [r1, r2, r3]
        shade = [d1,d2,d3]
        
        for i in range(max_iter):
            denom = (3 * z1 **2)
            if abs(denom) < epsilon:
                break
            z1 = z1 - (z1**3 - 1)/denom
            
        return shade[get_shade(z1, a)]
    
    def get_shade(z, roots):
        distance = [abs(z - root) for root in roots]
        min_index = distance.index(min(distance))
        return min_index
    return helper
hollusion(function_to_painter(newton_rap_frac(2/5, 1/2,3/5)))
# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
