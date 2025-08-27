from basisstrat import basisstrat
import random

class not_but_offset_by_three(basisstrat):

    def act(self, history_self, history_opponent):
        history_len = len(history_self)
        if (history_len <= 3):
            return random.choice([True, False])
        return not history_opponent[history_len - 4]