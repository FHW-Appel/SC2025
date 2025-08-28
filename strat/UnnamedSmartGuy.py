# DYNAMIC NICE
from basisstrat import basisstrat
import random

class UnnamedSmartGuy(basisstrat):
    STATIC = False
    DYNAMIC = True
    MEAN = False
    NICE = True
    RANDOM = False
    GRUDGING = False
    RETALIATING = True
    FORGIVING = True
    
    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE

        if history_self[:-1] == history_opponent[:-1] and history_opponent[-1] == self.COOPERATE:
            return self.COOPERATE

        consecutive_defections = 0
        for move in reversed(history_opponent):
            if move == self.DEFECT:
                consecutive_defections += 1
            else:
                consecutive_defections = 0
                break

        if consecutive_defections == 1 and history_opponent[-1] == self.COOPERATE:
            return self.COOPERATE

        if len(history_opponent) >= 2 and self.DEFECT in history_opponent[-2:]:
            return self.DEFECT

        if consecutive_defections >= 3 or (consecutive_defections == 2 and random.random() > 0.1):
            return self.COOPERATE
        
        if consecutive_defections >= 18:
            return self.DEFECT

        return self.COOPERATE
