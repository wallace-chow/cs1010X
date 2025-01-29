#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########
from math import *
def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))
import sys
# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6)) = 33
# Explanation: evaluated left to right, since there is no nested parenthesis, there is no
# thrice that takes presedence. thrice(thrice) would be compose(thrice, compose(thrice, thrice)),
#compose (thrice thrice) would be add1 9 times, compose(thrice, 9 times) would be add1 27 times, so 6+27 = 33


# (ii) print(thrice(thrice)(identity)(compose)) = compose address
# Explanation: thrice(thrice) is 27 times repeat of identity, then this is applied to compose, address of compose
# will be returned because the output is a function is 27 times of compose

# (iii) print(thrice(thrice)(sq)(1)) = 1
# Explanation: no precedence due to the parenthesis not favouring anything, so statement is evaluated left to right
# thrice(thrice)(sq) is square repeated 27 times, but squared applied 27 times is just 2^27 applied to the int input, 1**2**27 = 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: same explaination as iii, which gives 2**(2**27), i tried to increase max digit by importing sys but
# it lagged out my laptop so i will just leave this answer as valueerror.


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x in (0, 1):
            return x
        return 2 * x * x

    def op(x, y):
        return x + y

    n  = t + 1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        if x in (0, 1):
            return x
        return f(x - 1) + f(x - 2)

    def op(x, y):
        return max(x, y)

    return combine(f, op, n+1)
# Your answer here: yes, the operator would simply be max(x, y) LOL, kinda cheated but yes
