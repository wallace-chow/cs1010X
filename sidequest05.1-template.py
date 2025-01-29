#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *
#draw_points (200, unit_circle)
#draw_points (200 ,alternative_unit_circle)
##########
# Task 1 #
##########

# the density of points is skewed to the start of the circle, points are defined
# with changing gaps between each other on the alternative, while the points used
# to draw the unit_circle are evenly spaced out. This is because the alternative's definition inputs t^2 in sin and cos rather than sin, which
# means that in [0, 1] the gradient of the "time taken to draw the curve" will start from 0 ,and slowly increase to a gradient greater than the normal circle's "time taken to draw"
# hence the alternative uses points that starts off as almost next to each other, and the gap gradually increases to be greater than the gaps between the points used to draw the normal circle


##########
# Task 2 #
##########

# (a)
def spiral(t):
    """use polar equations, radius increase from 0 to 1, angle is represented by t*2pi"""
    return make_point(t*sin(2 * t* pi), t*cos(2 * t * pi))

#draw_connected_scaled(1000, spiral)

# (b)

def heart(t):
    def inverted_spiral(t):
        pt = spiral(t)
        return make_point(-x_of(pt), y_of(pt))
    if t <= 0.5:
        return spiral(2*t)
    if t > 0.5:
        return inverted_spiral(2*t - 1)
    

draw_connected_scaled(1000, heart)
