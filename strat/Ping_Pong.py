from basisstrat import basisstrat

class Ping_Pong(basisstrat):
    count = 0
    def act(self, history_self, history_opponent):
        if self.count == 0:
            self.count += 1
            return self.COOPERATE
        else:
            self.count = 0
            return self.DEFECT




