# STATIC nice

from basisstrat import basisstrat

class stupidniceman(basisstrat):
    STATIC = True
    DYNAMIC = False
    MEAN = False
    NICE = True
    RANDOM = False
    GRUDGING = False
    RETALIATING = False
    FORGIVING = False
    def act(self, history_self, history_opponent):
        return self.COOPERATE