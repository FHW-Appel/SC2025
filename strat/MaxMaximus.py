from basisstrat import basisstrat

class MaxMaximus(basisstrat):

    def act(self, history_self, history_opponent):
        if len(history_opponent) >= 2:            
            if history_opponent[-1] == self.COOPERATE and history_opponent[-2] == self.COOPERATE:
                return self.COOPERATE
                # gibt dem Gegner ein Chance
            
            else:
                return self.DEFECT

        else:
            return self.COOPERATE
            # Er Kooperiert in den ersten beiden Runden immer
        
