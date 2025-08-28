from basisstrat import basisstrat

class realerkenner(basisstrat):

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)

        if roundcounter >= 0 and roundcounter < 6:
            return self.COOPERATE
        elif roundcounter >= 6 and roundcounter < 12:
            return self.DEFECT
        else:
            if history_self == history_opponent:
                opponent = "self"
                print("Gespielt gegen sich selbst")
            elif history_opponent[0] == True and history_opponent[1] == False and history_opponent[2] == True and history_opponent[3] == True:
                opponent = "erkenner"
                print("Gespielt gegen erkenner/almostsmartniceman")
            elif sum(history_opponent[0:11]) == 0:
                opponent = "dagoberte"
                print("Gespielt gegen dagoberte")
            elif sum(history_opponent[0:11]) == 11:
                opponent = "stupidniceman"
                print("Gespielt gegen stupidniceman")
            elif sum(history_opponent[0:4]) == 4 and sum(history_opponent[5:11]) == 0:
                opponent = "nachtragend"
                print("Gespielt gegen nachtragend")
            elif history_opponent[0] == True and history_opponent[1] == False and history_opponent[2] == True and history_opponent[3] == False and history_opponent[4] == True and history_opponent[5] == False and history_opponent[6] == True and history_opponent[7] == False and history_opponent[8] == True and history_opponent[9] == False and history_opponent[10] == True:
                opponent = "Ping_Pong"
                print("Gespielt gegen Ping_Pong")
            elif history_opponent[0] == False and history_opponent[1] == True and history_opponent[2] == True and history_opponent[3] == False and history_opponent[4] == False and history_opponent[5] == False and history_opponent[6] == True and history_opponent[7] == False and history_opponent[8] == False and history_opponent[9] == True and history_opponent[10] == True:
                opponent = "bing_bong"
                print("Gespielt gegen bing_bong")
            elif history_self[roundcounter - 11:roundcounter - 1] == history_opponent[roundcounter - 10:roundcounter]:
                opponent = "vincentvariant"
                print("Gespielt gegen vincentvariant")
            else:
                opponent = "unknown"
                if roundcounter < 20:
                    return self.COOPERATE
            if opponent == "self" or opponent == "vincentvariant":
                return self.COOPERATE
            elif opponent == "erkenner" or opponent == "unknown" or opponent == "stupidniceman" or opponent == "dagoberte" or opponent == "nachtragend" or opponent == "Ping_Pong" or opponent == "bing_bong":
                return self.DEFECT
            else:
                return self.COOPERATE
