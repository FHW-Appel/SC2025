from basisstrat import basisstrat

class random_strat(basisstrat):

    def act(self, history_self, history_opponent):
        return self.random()