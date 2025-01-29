#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

## 27 long, 23 tall
##
def make_sans_undertale():
    a = [first(), second(), third_fourth(), third_fourth(), five_six(), five_six(), seven(), eight(), nine(), ten_eleven(), ten_eleven(), twelve(), thirteen(), fourteen(), fifteen(), sixteen(), seventeen(),
         eighteen(), nineteen(), twenty(), twenty1(), twenty2(), twenty3()]
    a = a[::-1]
    result = a[0]
    for i in range (1, 23):
        result = stack_frac(1/i, a[i], result)
    return result

def first ():
    x = beside_frac (4/7, blank_bb, black_bb)
    y = beside_frac (7/20, x, blank_bb)
    z = beside_frac (20/27, y, turn_upside_down(x))
    return z
def second():
    x = beside_frac(3/4, blank_bb, black_bb)
    y = beside_frac(4/23, x, blank_bb)
    z = beside_frac (23/27, y, turn_upside_down(x))
    return z
def third_fourth():
    x = beside_frac(2/3, blank_bb, black_bb)
    y = beside_frac (3/24, x, blank_bb)
    z = beside_frac(24/27, y, turn_upside_down(x))
    return z
def five_six():
    x = beside(blank_bb, black_bb)
    y = beside_frac(2/25, x, blank_bb)
    z = beside_frac(25/27, y, turn_upside_down(x))
    return z
def seven():
    x = beside_frac (1/26, black_bb, blank_bb)
    z = beside_frac(26/27, x, black_bb)
    return z
def eight():
    x = beside_frac(1/5, black_bb, blank_bb)
    y = beside (x, black_bb)
    z = beside_frac(10/17, y, blank_bb)
    w = beside_frac (17/27, z, turn_upside_down(y))
    return w
def nine():
    x = beside_frac (1/4, black_bb, blank_bb)
    y = beside_frac(4/11, x, black_bb)
    z = beside_frac(11/16, y, blank_bb)
    w = beside_frac (16/27, z, turn_upside_down(y))
    return w
def ten_eleven():
    def eye():
        a = beside_frac (1/3, black_bb, blank_bb)
        b = beside_frac (3/8, a, black_bb)
        return b
    x = beside_frac(1/3, black_bb, blank_bb)
    y = beside_frac (3/11, x, eye())
    c = beside_frac(11/16, y, blank_bb)
    z = beside_frac (16/24, c, eye())
    w = beside_frac (24/27, z, turn_upside_down(x))
    return w
def twelve():
    x = beside(blank_bb, black_bb)
    y = beside_frac(2/3, x, blank_bb)
    z = beside_frac (3/11, y, black_bb)
    w = beside_frac (11/13, z, blank_bb)
    d = beside_frac (13/14, w, black_bb)
    l = beside_frac(14/27, d, turn_upside_down(w))
    return l
def thirteen():
    x = beside(blank_bb, black_bb)
    y = beside_frac(2/9, x, blank_bb)
    z = beside_frac(9/10, y, black_bb)
    w = beside_frac(10/13, z, blank_bb)
    l = beside_frac(13/14, w, black_bb)
    o = beside_frac(14/27, l, turn_upside_down(w))
    return o
def fourteen():
    x = beside_frac(2/3, blank_bb, black_bb)
    y = beside_frac (3/7, x, blank_bb)
    z = beside_frac (7/9, y, black_bb)
    w = beside_frac (9/12, z, blank_bb)
    l = beside_frac (12/13, w, black_bb)
    f = beside_frac (13/14, l, black_bb)
    o = beside_frac (14/27, f, turn_upside_down(l))
    return o
def fifteen():
    x = beside_frac(2/3, blank_bb, black_bb)
    y = beside(x, x)
    z = beside(y, blank_bb)
    o = beside_frac(12/13, z, black_bb)
    l = beside_frac(13/14, o, black_bb)
    f = beside_frac(14/27, l, turn_upside_down(o))
    return f
def sixteen():
    x = beside (blank_bb, black_bb)
    y = beside_frac (2/5, x, blank_bb)
    z = beside_frac (5/7, y, black_bb)
    w = beside_frac (7/21, z, blank_bb)
    l = beside_frac (21/23, w, black_bb)
    o = beside_frac (23/25, l, blank_bb)
    p = beside_frac (25/27, o, beside(black_bb, blank_bb))
    return p
def seventeen():
    x = beside(blank_bb, black_bb)
    y = beside_frac(2/6, x, beside(blank_bb, black_bb))
    z = beside_frac(6/9, y, beside_frac(1/3, blank_bb, black_bb))
    w = beside_frac (9/19, z, blank_bb)
    o = beside_frac(19/24, w, black_bb)
    l = beside_frac(24/26, o, beside(blank_bb, black_bb))
    p = beside_frac (26/27, l, blank_bb)
    return p
def eighteen():
    x = beside(blank_bb, black_bb)
    y = beside_frac(2/5, x, blank_bb)
    z = beside_frac (5/9, y, beside(beside(black_bb, blank_bb),beside(black_bb, blank_bb)))
    w = beside_frac (9/19, z, black_bb)
    o = beside_frac(19/22, w, beside_frac(1/3, blank_bb, black_bb))
    l = beside_frac (22/26, o, beside_frac(3/4, blank_bb, black_bb))
    p = beside_frac (26/27, l, blank_bb)
    return p
def nineteen():
    a = beside_frac(2/3, blank_bb, black_bb)
    b = beside_frac(3/8, a, beside_frac(3/5, blank_bb, black_bb))
    c = beside_frac(2/3, blank_bb, black_bb)
    d = beside_frac(8/11, b, c)
    x = beside_frac(11/14, d, c)
    w = beside_frac(14/17, x, c)
    e = beside_frac(17/21, w, beside(beside(blank_bb, black_bb),beside(blank_bb, black_bb)))
    f = beside_frac(21/25, e, beside_frac(3/4, blank_bb, black_bb))
    g = beside_frac(25/27, f, blank_bb)
    return g
def twenty():
    a = beside_frac(2/3, blank_bb, black_bb)
    b = beside_frac (3/9, a, beside_frac (2/3, blank_bb, black_bb))
    c = beside_frac (9/11, b, beside(blank_bb, black_bb))
    c1 = beside_frac(2/3, blank_bb, black_bb)
    x = beside_frac(11/14, c, c1)
    y = beside_frac(14/17, x, c1)
    d = beside_frac(17/20, y, c1)
    e = beside_frac(20/24, d, blank_bb)
    f = beside_frac(24/27, e, turn_upside_down(c1))
    return f
def twenty1():
    x = beside_frac(3/4, blank_bb, black_bb)
    y = beside_frac(4/19, x, beside_frac(5/15, blank_bb, black_bb))
    z = beside_frac(19/27, y, beside(blank_bb, beside_frac(1/4, black_bb, blank_bb)))
    return z
def twenty2():
    x = beside_frac(4/6, blank_bb, black_bb)
    y = beside_frac(6/21, x, blank_bb)
    z = beside_frac (21/27, y, beside_frac(2/6, black_bb, blank_bb))
    return z
def twenty3():
    x = beside_frac(6/9, blank_bb, black_bb)
    y = beside_frac (9/21, x, beside_frac(9/12, blank_bb, black_bb))
    z = beside_frac (21/27, y, blank_bb)
    return z

def beside_frac(a, pic1, pic2):
    x = quarter_turn_right(pic1)
    y = quarter_turn_right(pic2)
    z = stack_frac(a, x, y)
    return quarter_turn_left (z)

# You may submit up to 3 entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.


show(make_sans_undertale())



