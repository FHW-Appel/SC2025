# STATIC random
from basisstrat import basisstrat
import random

class random_strat(basisstrat):
    STATIC = True
    random = True
    def act(self, history_self, history_opponent):
        return random.choice([True, False])