# STATIC MEAN
from basisstrat import basisstrat

class bing_bong(basisstrat):
    STATIC = True
    DYNAMIC = False
    MEAN = True
    NICE = False
    RANDOM = False
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False

    pattern = "011000100110100101101110011001110010000001100010011011110110111001100111"

    def act(self, history_self, history_opponent):
        len_history = len(history_self)
        len_pattern = len(self.pattern)
        move = self.pattern[len_history % len_pattern]
        
        return move == '1'
