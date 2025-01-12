#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree (n, pic):
    
    if n < 1:
        pass
    
    elif n == 1:
        return pic
#initialise variable
    product = pic
    for k in range(2, n + 1):
        product = overlay_frac (1 / k, scale((n + 1 - k) / n, pic), product)
    return product
# Test x = 1, n = 4

show(tree(4, circle_bb))


##########
# Task 2 #
##########
# translate(0.1, 0.15, heart_bb))

def helix (pic, n):
    if n < 5:
        pass
#set up abstracted variables
    pic_list = []
    r = 1 / 2 - 1 / n
    scaled_pic = scale (2 / n, pic)
    
    for i in range (n - 1, -1, -1):
        rad = i * (2 * math.pi / n)
        x_coord = math.sin(rad) * r
        y_coord = math.cos(rad) * r
        pic_list.append (translate (x_coord, y_coord, scaled_pic))
#need a function similar to tree actually but takes in a list
    return make_circle(pic_list)


def make_circle (arr):
#initialise varivales
    fraction = 1
    product = arr[0]
    arr.pop(0)
    
    for k in arr:
        fraction += 1
        product = overlay_frac (1 / fraction, k, product)

    return product

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)



# Test
#show(helix(make_cross(rcross_bb), 25))

