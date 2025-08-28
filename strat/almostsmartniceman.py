from basisstrat import basisstrat

class almostsmartniceman(basisstrat):

    STATIC = False
    DYNAMIC = True
    MEAN = True
    NICE = False
    RANDOM = True
    GRUDGING = False
    RETALIATING = True
    FORGIVING = True

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)
        if roundcounter == 0:
            return self.COOPERATE
        elif roundcounter == 2:
            return self.COOPERATE
        elif roundcounter == 3:
            return self.COOPERATE
        elif roundcounter > 5 and history_self == history_opponent:
             return self.COOPERATE
        elif roundcounter >= 5 and sum(history_opponent[-5:]) == 0:
            return self.DEFECT
        elif history_opponent[roundcounter - 1] == self.COOPERATE:
            return self.COOPERATE
        else:
            return self.DEFECT