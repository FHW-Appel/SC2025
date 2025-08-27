from basisstrat import basisstrat
from simulation import *
from random import choice, randint

class zurueckschauend(basisstrat):

    def act(self, history_self, history_opponent):
        roundcounter = len(history_opponent)
        if roundcounter == 1:
            return self.DEFECT
        if roundcounter == 2:
            return self.COOPERATE
        if roundcounter >= 8:
            if sum(history_opponent[-6:]) == 0:    #history_opponent[roundcounter] ==  history_opponent[roundcounter-1] == history_opponent[roundcounter - 2] == history_opponent[roundcounter - 3] == history_opponent[roundcounter - 4] == history_opponent[roundcounter - 5] == False:
                return self.DEFECT
            elif sum(history_opponent[-6:]) == 6:  #history_opponent[roundcounter] ==  history_opponent[roundcounter-1] == history_opponent[roundcounter - 2] == history_opponent[roundcounter - 3] == history_opponent[roundcounter - 4] == history_opponent[roundcounter - 5] == True:
                return self.COOPERATE
            else:
                history_opponent_choice = history_opponent[roundcounter - 2]
                randomnumber = randint(0,1)
                if history_opponent_choice == False:
                    if roundcounter % 2 == 0:
                        return self.COOPERATE
                    elif randomnumber == 0:
                        return self.DEFECT
                    else:
                        return self.DEFECT
                elif history_opponent_choice == True:
                    if roundcounter % 2 == 0:
                        return self.DEFECT
                    elif randomnumber == 0:
                        return self.COOPERATE
                    else:
                        return self.DEFECT
        else:
            return self.DEFECT