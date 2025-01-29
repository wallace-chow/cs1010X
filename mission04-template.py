#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y : (Number) -> curve

# (b)
# your answer here a_line : (Number) -> Point

# (c)
def vertical_line(point, length):
    y = y_of(point)
    x = x_of(point)
    return lambda t: make_point(x, t * length + y) 

draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))


# (d)
# your answer here vertical_line : (point, number) -> curve

# (e)
# your answer here draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# your answer here: they are vertically symmetrical

# (b) since f(a - x) = f(a + x) => f(2a - x) = f(x) for symmetry about x = 0.5, i can just transform f(x) to f(1 - x), with a = 0.5
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        ## parametric: x = sin(2pi t) , y= cos(2pi t)
        return make_point(-x_of(curve(t)) , y_of(curve(t)))
    return reflected_curve
	
draw_connected_scaled(200, arc)
draw_connected_scaled(200, reflect_through_y_axis(arc))
draw_connected_scaled(200, reflect_through_y_axis(vertical_line(make_point(0.1, 0.1), 0.4)))
