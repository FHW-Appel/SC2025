# STATIC random
from basisstrat import basisstrat

class random_strat(basisstrat):
    STATIC = True
    random = True
    def act(self, history_self, history_opponent):
        return self.random()