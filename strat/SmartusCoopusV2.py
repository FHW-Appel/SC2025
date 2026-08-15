# DYNAMIC NICE
from basisstrat import basisstrat


class SmartusCoopusV2(basisstrat):
    STATIC = False
    DYNAMIC = True
    MEAN = False
    NICE = True
    RANDOM = False
    GRUDGING = False
    RETALIATING = True
    FORGIVING = True

    ROUNDS = 200

    def act(self, mine, theirs):
        turn = len(mine)

        if turn == 0:
            return self.COOPERATE

        if turn == self.ROUNDS - 1:
            return self.DEFECT

        if theirs[0] == self.DEFECT:
            return self.DEFECT

        if theirs[:2] == [self.COOPERATE, self.DEFECT]:
            if turn in (2, 3):
                return self.DEFECT
            if turn == 4:
                return self.COOPERATE

        bad = [i for i, move in enumerate(theirs) if move == self.DEFECT]

        if not bad:
            return self.COOPERATE

        first_bad = bad[0]
        if (
            first_bad >= 5
            and turn >= first_bad + 4
            and theirs[first_bad:first_bad + 4] == [self.DEFECT] * 4
        ):
            return theirs[-1]

        if turn >= 11 and self._copies(mine, theirs):
            return self.COOPERATE

        ignored, answered = self._after_our_defects(mine, theirs)

        if ignored and not answered:
            return self.DEFECT

        if (
            not ignored
            and not answered
            and turn >= 8
            and mine[-3:] == [self.COOPERATE] * 3
            and theirs[-3:] == [self.COOPERATE] * 3
        ):
            return self.DEFECT

        if turn >= 4 and mine[-4:] == [self.DEFECT] * 4:
            return self.DEFECT

        if self._gaps_grow(bad):
            return self.DEFECT

        if turn >= 8 and self._repeats(theirs):
            return self.DEFECT

        if turn >= 7 and self._does_opposite(mine, theirs):
            return self.DEFECT

        if turn >= 12 and len(bad) / turn >= 0.5:
            return self.DEFECT

        return self.COOPERATE

    @staticmethod
    def _after_our_defects(mine, theirs):
        ignored = 0
        answered = 0

        for i in range(5, len(mine) - 1):
            if mine[i] == basisstrat.DEFECT:
                if theirs[i + 1] == basisstrat.COOPERATE:
                    ignored += 1
                else:
                    answered += 1

        return ignored, answered

    @staticmethod
    def _copies(mine, theirs):
        start = max(1, len(theirs) - 12)
        count = len(theirs) - start

        if count < 10:
            return False

        matches = sum(
            theirs[i] == mine[i - 1]
            for i in range(start, len(theirs))
        )

        return matches >= count - 1

    @staticmethod
    def _does_opposite(mine, theirs):
        start = max(1, len(theirs) - 6)
        count = len(theirs) - start

        if count < 5:
            return False

        return all(
            theirs[i] != mine[i - 1]
            for i in range(start, len(theirs))
        )

    @staticmethod
    def _repeats(history):
        recent = history[-8:]

        for size in range(1, 5):
            if all(
                recent[i] == recent[i % size]
                for i in range(len(recent))
            ):
                return basisstrat.DEFECT in recent

        return False

    @staticmethod
    def _gaps_grow(bad):
        if len(bad) < 4:
            return False

        a, b, c, d = bad[:4]
        gap1 = b - a
        gap2 = c - b
        gap3 = d - c

        return (
            gap1 >= 2
            and gap2 == gap1 + 2
            and gap3 == gap2 + 2
        )