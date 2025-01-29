#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    x_diff = x_of(curve1(1)) - x_of(curve2(0))
    y_diff = y_of(curve1(1)) - y_of(curve2(0))
    translated_curve = translate(x_diff, y_diff)(curve2)
    return connect_rigidly(curve1, translated_curve)
        

##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect (- 0.5, -0.5, 1.5, 1.5)(gosper_arbitrary(level, initial_curve))
    return draw_points(num_points, squeezed_curve)
def gosper_arbitrary(level, curve):
    return repeated(gosperize, level)(curve)
#show_points_gosper(5, 500, arc)
##########
# Task 3 #
##########
'''def gosperize_with_angle ( theta ):
        def inner_gosperize ( curve ):
            scale_factor = ( 1 / cos ( theta )) / 2
            scaled_curve = scale ( scale_factor )( curve )
            left_curve = rotate ( theta )( scaled_curve )
            right_curve = translate ( 0 .5 , sin ( theta )* scale_factor ) \
            ( rotate ( - theta )( scaled_curve ))
            return connect_rigidly ( left_curve , right_curve )
        return inner_gosperize'''
def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))\
               (your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    '''scales, translates and connects rigidly - translating to connect \
can be done by connect ends and put_in
    i need to scale and rotate the curve'''
    def inner_gosperize(curve_fn):
        scale_factor = (1 / cos(theta)) / 2
        scaled_curve = scale (scale_factor)(curve_fn)
        left_curve = rotate (theta)(scaled_curve)
        right_curve = rotate(-theta)(scaled_curve)
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
