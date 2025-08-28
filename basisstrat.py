from random import choice

class basisstrat:
    COOPERATE: bool = True
    DEFECT: bool = False

    def act(self, history_self, history_opponent):
        return self.COOPERATE

    def random(self) -> bool:
        return choice([basisstrat.COOPERATE, basisstrat.DEFECT])