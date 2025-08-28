from basisstrat import basisstrat
import random
import math

class ichglaubeselbstnichtdran(basisstrat):
    """
    Ein einfaches neuronales Netz, das während des Spiels dazulernt.
    Kein PyTorch, nur NumPy.
    """
    def __init__(self):
        # 4 Eingaben: eigene letzten 2 Züge, gegnerische letzten 2 Züge
        # 1 verstecktes Neuron, 1 Ausgang (Sigmoid)
        self.weights = [random.uniform(-1, 1) for _ in range(5)]  # 4 Inputs + 1 Bias
        self.learning_rate = 0.1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_deriv(self, x):
        sx = self.sigmoid(x)
        return sx * (1 - sx)

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)

        # Initial: kooperativ starten
        if roundcounter < 2:
            return self.COOPERATE

        # Eingaben: eigene letzten 2, gegnerische letzten 2 (True=1, False=0)
        inputs = [
            int(history_self[-2]),
            int(history_self[-1]),
            int(history_opponent[-2]),
            int(history_opponent[-1])
        ]
        bias = 1

        # Vorwärtsdurchlauf
        z = sum(w * i for w, i in zip(self.weights[:-1], inputs)) + self.weights[-1] * bias
        output = self.sigmoid(z)

        # Entscheidung: Schwelle 0.5
        action = self.COOPERATE if output >= 0.5 else self.DEFECT

        # Lernen: falls genug History vorhanden
        if roundcounter >= 3:
            # Ziel: mache das, was im letzten Zug am meisten gebracht hätte
            # Wenn Gegner kooperiert hat, wäre Kooperation besser gewesen, sonst Defektion
            target = int(history_opponent[-1])  # 1 für C, 0 für D

            # Backpropagation für 1 Neuron
            error = target - output
            for i in range(4):
                self.weights[i] += self.learning_rate * error * inputs[i]
            self.weights[-1] += self.learning_rate * error * bias

        return action