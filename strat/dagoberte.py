# STATIC MEAN

from basisstrat import basisstrat

class dagoberte(basisstrat):
    STATIC = True
    DYNAMIC = False
    MEAN = True
    NICE = False
    RANDOM = False
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False
    def act(self, history_self, history_opponent):
        return self.DEFECT