from basisstrat import basisstrat
import random

class random_strat(basisstrat):

    def act(self, history_self, history_opponent):
        return random.choice([True, False])