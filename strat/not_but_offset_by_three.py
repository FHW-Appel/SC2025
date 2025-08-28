# dynamic random 

from basisstrat import basisstrat
import random

class not_but_offset_by_three(basisstrat):
    STATIC = False
    DYNAMIC = True
    MEAN = False
    NICE = False
    RANDOM = True
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False
    def act(self, history_self, history_opponent):
        history_len = len(history_self)
        if (history_len <= 3):
            return random.choice([True, False])
        return not history_opponent[history_len - 4]