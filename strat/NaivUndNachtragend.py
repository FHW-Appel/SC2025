from basisstrat import basisstrat

class NaivUndNachtragend(basisstrat):
    STATIC = False
    DYNAMIC = True
    MEAN = False
    NICE = True
    RANDOM = False
    GRUDGING = True
    RETALIATING = True
    FORGIVING = False

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        else:
            anzahl_false = history_opponent.count(False)
            if anzahl_false < 3:
                return self.COOPERATE
            else:
                return self.DEFECT
