class basisstrat:
    COOPERATE: bool = True
    DEFECT: bool = False

    def act(self, history_self, history_opponent):
        return self.COOPERATE