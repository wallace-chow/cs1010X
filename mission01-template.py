#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(a, b, c, d):
    x = stack (a, b)
    y = stack (d, c)
    return beside(y, x)


# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(pic):
    x = stack (pic, pic)
    return beside (pic, x)

# Test
#show(simple_fractal(make_cross(rcross_bb)))
