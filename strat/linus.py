import math
from basisstrat import basisstrat

def is_perfect_square(num):
    square_root = math.isqrt(num)
    return square_root * square_root == num



class linus(basisstrat):

    def act(self, history_self, history_opponent):
        if is_perfect_square(len(history_self)):
            return self.DEFECT
        else:
            return self.COOPERATE
        
