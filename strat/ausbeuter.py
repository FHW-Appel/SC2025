from basisstrat import basisstrat

class ausbeuter(basisstrat):
    NICE = False

    def act(self, history_self, history_opponent):
        if len(history_opponent) == 0:
            return self.COOPERATE
        
        if history_opponent[-1:] == [self.COOPERATE, self.COOPERATE, self.COOPERATE, self.COOPERATE]:
            return self.DEFECT

        if history_opponent[-1] == self.DEFECT:
            return self.DEFECT

        if history_opponent[-1] == self.COOPERATE and history_self[-1] == self.DEFECT:
            return self.DEFECT

        return self.COOPERATE
