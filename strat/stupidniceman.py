# STATIC nice

from basisstrat import basisstrat

class stupidniceman(basisstrat):
    STATIC = True
    nice = True
    def act(self, history_self, history_opponent):
        return self.COOPERATE