from basisstrat import basisstrat

class TitForTat(basisstrat):

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        else:
            return history_opponent[-1]