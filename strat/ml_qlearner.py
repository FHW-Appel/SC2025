from basisstrat import basisstrat
import random

class ml_qlearner(basisstrat):
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.01
        self.gamma = 0.85
        self.epsilon = 0.1
        self.memory = 12
        self.last_state = None
        self.last_action = None

    def get_state(self, history_self, history_opponent):
        s = tuple((history_self + [True]*self.memory)[-self.memory:])
        o = tuple((history_opponent + [None]*self.memory)[-self.memory:])
        return s + o

    def act(self, history_self, history_opponent):
        state = self.get_state(history_self, history_opponent)
        if state not in self.q_table:
            self.q_table[state] = [0.0, 0.0]

        if random.random() < self.epsilon:
            action = self.random()
        else:
            q_coop, q_def = self.q_table[state]
            action = self.COOPERATE if q_coop >= q_def else self.DEFECT

        if self.last_state is not None and self.last_action is not None:
            if len(history_self) > 0:
                last_opp_action = history_opponent[-1]
                last_self_action = history_self[-1]
                if last_self_action and last_opp_action:
                    reward = 3
                elif not last_self_action and not last_opp_action:
                    reward = 1
                elif last_self_action and not last_opp_action:
                    reward = 0
                else:
                    reward = 5

                prev_q = self.q_table[self.last_state][0 if self.last_action == self.COOPERATE else 1]
                max_next_q = max(self.q_table[state])
                new_q = prev_q + self.learning_rate * (reward + self.gamma * max_next_q - prev_q)
                self.q_table[self.last_state][0 if self.last_action == self.COOPERATE else 1] = new_q

        self.last_state = state
        self.last_action = action
        return action