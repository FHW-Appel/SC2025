from basisstrat import basisstrat

class gegenteil(basisstrat):

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        return not history_opponent[-1]