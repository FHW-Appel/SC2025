from basisstrat import basisstrat

class gegenteil(basisstrat):

    def act(self, history_self, history_opponent):
        return not history_opponent[-1]