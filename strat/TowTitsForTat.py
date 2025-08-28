from basisstrat import basisstrat

class TowTitsForTat(basisstrat):
    """
    First cooperates, then defects twice if the
    opponent has defected in the last two moves.
    """

    def act(self, history_self, history_opponent):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if len(history_self) < 1:
            return self.COOPERATE
        if len(history_self) < 2:
            if history_opponent[-1] == self.DEFECT:
                return self.DEFECT
            else:
                return self.COOPERATE
        if history_opponent[-1] == self.DEFECT or history_opponent[-2] == self.DEFECT:
            return self.DEFECT
        else:
            return self.COOPERATE
