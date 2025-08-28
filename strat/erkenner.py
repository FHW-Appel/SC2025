from basisstrat import basisstrat

class erkenner(basisstrat):

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        elif len(history_self) == 1:
            return self.DEFECT
        elif len(history_self) == 2:
            return self.COOPERATE
        elif len(history_self) == 3:
            return self.COOPERATE
        elif history_self[:-1] == history_opponent[1:]:
            return self.COOPERATE
        elif len(history_self) > 5 and history_self == history_opponent:
             return self.COOPERATE
        elif len(history_self) > 5 and history_opponent[0] == 1 and history_opponent[1] == 1 and history_opponent[2] == 0 and history_opponent[3] == 0 and history_opponent[4] == 1:
            return self.COOPERATE
        else:
            return self.DEFECT

