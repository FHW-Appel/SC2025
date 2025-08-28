from basisstrat import basisstrat
import random


class Joss(basisstrat):
    '''
    Spielt Tit for Tat, beginnt mit Kooperation.
    In 10% der Fälle wird hinterhältig defected.
    '''
    NICE = False

    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        else:
            if history_opponent[-1] == self.DEFECT:
                return self.DEFECT
            else:
                # Mit 10% Wahrscheinlichkeit hinterhältig defektieren
                if random.random() < 0.1:
                    return self.DEFECT
                else:
                    return self.COOPERATE
                 