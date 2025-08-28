# STATIC MEAN

from basisstrat import basisstrat

class dagoberte(basisstrat):
    STATIC = True
    MEAN = True
    def act(self, history_self, history_opponent):
        return self.DEFECT