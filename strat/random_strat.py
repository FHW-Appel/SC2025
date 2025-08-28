# STATIC random
from basisstrat import basisstrat
import random

class random_strat(basisstrat):
    STATIC = True
    DYNAMIC = False
    MEAN = False
    NICE = False
    RANDOM = True
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False
    def act(self, history_self, history_opponent):
        return random.choice([True, False])