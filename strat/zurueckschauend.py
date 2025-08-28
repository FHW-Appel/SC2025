from basisstrat import basisstrat
from simulation import *
from random import choice, randint

class zurueckschauend(basisstrat):
    STATIC = False
    DYNAMIC = True
    MEAN = True
    NICE = False
    RANDOM = True
    GRUDGING = False
    RETALIATING = True
    FORGIVING = True
    def act(self, history_self, history_opponent):
        roundcounter = len(history_opponent)
        if roundcounter == 0:
            return self.DEFECT
        elif roundcounter == 1:
            return self.COOPERATE
        elif roundcounter == 2:
            return history_opponent[roundcounter - 1]
        elif roundcounter >= 6:
            if sum(history_opponent[-6:]) == 0:
                return self.DEFECT
            elif sum(history_opponent[-6:]) == 6 and sum(history_self[-2:]) != 2: 
                return self.COOPERATE
            elif sum(history_opponent[-6:]) == 6 and sum(history_self[-2:]) == 2: 
                return self.DEFECT
            else:
                randomnumber = randint(0,2)
                if roundcounter % 2 == 0:
                    return history_opponent[roundcounter - 2]
                elif randomnumber == 0:
                    return not history_opponent[roundcounter - 2]
                else:
                    return self.DEFECT
        else:
            return self.DEFECT