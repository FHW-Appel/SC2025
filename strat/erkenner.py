from basisstrat import basisstrat

class erkenner(basisstrat):

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
          return self.COOPERATE
        elif len(history_self) == 1:
          return self.DEFECT
        elif history_self[:-1] == history_opponent[1:]:
          return self.COOPERATE
        elif len(history_self) > 5 and history_self == history_opponent:
          return self.COOPERATE
        else:
          return self.DEFECT
