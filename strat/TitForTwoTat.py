from basisstrat import basisstrat

class TitForTwoTat(basisstrat):
    """
    First cooperates, then defects only if the 
    opponent has defected in the last two moves.    
    """

    def act(self, history_self, history_opponent):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if len(history_self) < 2:
            return self.COOPERATE
        else:
            if history_opponent[-1] == self.DEFECT and history_opponent[-2] == self.DEFECT:
                return self.DEFECT
            else:
                return self.COOPERATE