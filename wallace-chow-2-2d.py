#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *
from graphics import *
########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 3 of 3
# ============

def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci (n - 2)

def foo(pic, n):
    a = [True, False, False, False] ##right, top, left, bottom
    term = pic
    for i in range(1, n + 1):
        if a[0]:
            a[0] = not a[0]
            if i == 1:
                term = beside (pic, pic)
            else:
                term = beside_frac (fibonacci(i - 1) / fibonacci(i + 1), term, pic)
            a[1] = not a[1]
        elif a[1]:
            a[1] = not a[1]
            term = stack_frac (fibonacci(i) / fibonacci(i + 1), pic, term)
            a[2] = not a[2]
        elif a[2]:
            a[2] = not a[2]
            term = beside_frac (fibonacci(i) / fibonacci(i + 1), pic, term)
            a[3] = not a[3]
        elif a[3]:
            a[3] = not a[3]
            term = stack_frac(fibonacci (i - 1) / fibonacci (i + 1), term, pic)
            a[0] = not a[0]
    return term

def beside_frac(a, pic1, pic2):
    x = quarter_turn_right(pic1)
    y = quarter_turn_right(pic2)
    z = stack_frac(a, x, y)
    return quarter_turn_left (z)


##make a right turn, combine and then left turn
show (foo(nova_bb, 8))




