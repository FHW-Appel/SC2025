from basisstrat import basisstrat

class antierkenner(basisstrat):

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)
        if roundcounter == 0:
            return self.DEFECT
        elif roundcounter == 1:
            return self.DEFECT
        elif roundcounter == 2:
            return self.DEFECT
        elif roundcounter == 3:
            return self.DEFECT
        elif len(history_self) > 5 and history_self == history_opponent:
             return self.COOPERATE
        else:
            return self.DEFECT