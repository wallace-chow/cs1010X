#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    if n <= 0:
        pass
    def helper (pic, x):
        if x == 0:
            return pic
        pic1 = stackn (2, pic)
        return beside (pic, helper (pic1, x - 1))

    return helper(pic, n - 1)

# Test
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    pic1 = stackn (2 ** (n - 1), pic)
    for x in range(n - 2, -1, -1):
        pic1 = beside (stackn (2 ** x, pic), pic1)
    return pic1

# Test
#show(fractal_iter(make_cross(rcross_bb), 3))
#show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n < 1:
        pass
    
    def helper (a, b, x):        
        if x == 0:
            return a
        b = stackn(2, b)
        c = stackn(2, a)
        return beside(a, helper(b, c, x - 1))
            

    return helper(pic1, pic2, n - 1)
    
   

# Test
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    if n == 1:
        return pic1
    a = (pic2, pic1)
    proto = stackn ( 2 ** (n - 1), a[n % 2])
    for x in range (n - 2, -1, -1):
        pic_in_posx = a[(x - 1) % 2]
        proto = beside(stackn (2 ** x, pic_in_posx), proto)
    return proto
    

# Test
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########
a = []
def steps(pic1, pic2, pic3, pic4):
    
    a = [pic1, pic2, pic3, pic4]
    for x in range(4):
        a[x] = position(a[x], x)
        
    return layer(a)

def position (pic, pos):
    
    if pos == 0:
        step1 = beside (blank_bb, pic)
        step2 = stack_frac(1/2, step1, blank_bb)
        
    elif pos == 1:
        step1 = beside (blank_bb, pic)
        step2 = stack_frac(1/2, blank_bb, step1)
        
    elif pos == 2:
        step1 = beside (pic, blank_bb)
        step2 = stack_frac (1 / 2, blank_bb, step1)
        
    elif pos == 3:
        step1 = beside (pic, blank_bb)
        step2 = stack_frac (1 / 2, step1, blank_bb)
        
    return step2

def layer(a):
    return overlay (overlay (a[3], a[2]), overlay (a[1], a[0]))
    



# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
