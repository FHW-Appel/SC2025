from basisstrat import basisstrat

class nachtragend(basisstrat):
    
    def act(self, history_self, history_opponent):
        if len(history_self) == 0:
            return self.COOPERATE
        
        else:    
            if sum(history_opponent) == len(history_opponent):
                print("Geht")
                return self.COOPERATE
            else:
                return self.DEFECT