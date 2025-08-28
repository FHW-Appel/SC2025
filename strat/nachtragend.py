from basisstrat import basisstrat

class nachtragend(basisstrat):
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
            if sum(history_opponent) == len(history_opponent):
                return self.COOPERATE
            else:
                return self.DEFECT