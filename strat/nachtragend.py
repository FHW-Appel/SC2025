from basisstrat import basisstrat

class nachtragend(basisstrat):
    nice = True
    dynamic = True
    
    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        else:    
            return history_opponent[0]