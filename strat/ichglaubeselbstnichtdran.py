from basisstrat import basisstrat
import random
import math

class ichglaubeselbstnichtdran(basisstrat):
    """
    Ein kleines neuronales Netz mit mehreren Neuronen im Hidden-Layer,
    das während des Spiels dazulernt. Kein PyTorch, nur NumPy.
    """
    def __init__(self):
        self.input_size = 6  # Letzte 2 Aktionen von beiden Spielern (2 + 2) + Vorletzte 2 Aktionen von beiden Spielern (2 + 2)
        self.hidden_size = 50  # Mehr Neuronen im Hidden-Layer
        self.output_size = 1

        # Gewichte für Input -> Hidden (hidden_size x input_size)
        self.weights_ih = [[random.uniform(-1, 1) for _ in range(self.input_size)] for _ in range(self.hidden_size)]
        # Bias für Hidden
        self.bias_h = [random.uniform(-1, 1) for _ in range(self.hidden_size)]

        # Gewichte für Hidden -> Output (output_size x hidden_size)
        self.weights_ho = [random.uniform(-1, 1) for _ in range(self.hidden_size)]
        # Bias für Output
        self.bias_o = random.uniform(-1, 1)
        self.learning_rate = 0.1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_deriv(self, x):
        sx = self.sigmoid(x)
        return sx * (1 - sx)

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)

        # Initial: kooperativ starten
        if roundcounter < 4:
            return self.COOPERATE

        # Eingaben: eigene letzten 4, gegnerische letzten 4 (True=1, False=0)
        inputs = [
            #int(history_self[-4]),
            int(history_self[-3]),
            int(history_self[-2]),
            int(history_self[-1]),
            #int(history_opponent[-4]),
            int(history_opponent[-3]),
            int(history_opponent[-2]),
            int(history_opponent[-1])

        ]

        # Vorwärtsdurchlauf: Input -> Hidden
        hidden = []
        for h in range(self.hidden_size):
            z = sum(w * i for w, i in zip(self.weights_ih[h], inputs)) + self.bias_h[h]
            hidden.append(self.sigmoid(z))

        # Hidden -> Output
        z_out = sum(w * h for w, h in zip(self.weights_ho, hidden)) + self.bias_o
        output = self.sigmoid(z_out)

        # Entscheidung: Schwelle 0.5
        action = self.COOPERATE if output >= 0.5 else self.DEFECT

        # Lernen: falls genug History vorhanden
        if roundcounter >= 4:
            target = int(history_opponent[-1])  # 1 für C, 0 für D
            error = target - output

            # Output Layer Gradienten
            d_output = error * self.sigmoid_deriv(z_out)

            # Update Hidden -> Output Gewichte und Bias
            for h in range(self.hidden_size):
                self.weights_ho[h] += self.learning_rate * d_output * hidden[h]
            self.bias_o += self.learning_rate * d_output

            # Hidden Layer Gradienten und Update Input -> Hidden Gewichte und Bias
            for h in range(self.hidden_size):
                d_hidden = d_output * self.weights_ho[h] * self.sigmoid_deriv(
                    sum(w * i for w, i in zip(self.weights_ih[h], inputs)) + self.bias_h[h]
                )
                for i in range(self.input_size):
                    self.weights_ih[h][i] += self.learning_rate * d_hidden * inputs[i]
                self.bias_h[h] += self.learning_rate * d_hidden

        return action