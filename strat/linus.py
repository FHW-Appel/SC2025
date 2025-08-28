# STATIC MEAN

import math
from basisstrat import basisstrat

def is_perfect_square(num):
    square_root = math.isqrt(num)
    return square_root * square_root == num



class linus(basisstrat):
    STATIC = True
    DYNAMIC = False
    MEAN = True
    NICE = False    
    RANDOM = False
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False
    def act(self, history_self, history_opponent):
        if is_perfect_square(len(history_self)+1):
            return self.DEFECT
        else:
            return self.COOPERATE
        
