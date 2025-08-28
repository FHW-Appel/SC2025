# STATIC MEAN
from basisstrat import basisstrat
import random

class NiceGuyCooper(basisstrat):
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
        
        defections = sum(1 for move in history_opponent if move == self.DEFECT)
        
        if defections == 1 and history_opponent[-1] == self.COOPERATE:
            return self.COOPERATE
        
        if history_opponent[-1] == self.DEFECT or history_opponent[-2] == self.DEFECT:
            return self.DEFECT

        if defections >= 5 or history_opponent[-1] == self.DEFECT and random.random() > 0.1:
            return self.DEFECT
        
        return self.COOPERATE