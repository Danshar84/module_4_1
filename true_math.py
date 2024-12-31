import math
from math import inf
def divide(first, second):
    b=0
    if second == 0:
        b = math.inf
    else:
        b = first / second
    return b
