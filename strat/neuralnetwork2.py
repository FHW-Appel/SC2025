from basisstrat import basisstrat
import random
import math

class neuralnetwork2(basisstrat):
    """
    Ein neuronales Netz mit fünf Hidden-Layers, das während des Spiels dazulernt.
    """
    def __init__(self):
        self.input_size = 6
        self.hidden1_size = 64
        self.hidden2_size = 64
        self.hidden3_size = 48
        self.hidden4_size = 32
        self.hidden5_size = 16
        self.output_size = 1

        # Input -> Hidden1
        self.weights_ih1 = [[random.uniform(-1, 1) for _ in range(self.input_size)] for _ in range(self.hidden1_size)]
        self.bias_h1 = [random.uniform(-1, 1) for _ in range(self.hidden1_size)]

        # Hidden1 -> Hidden2
        self.weights_h1h2 = [[random.uniform(-1, 1) for _ in range(self.hidden1_size)] for _ in range(self.hidden2_size)]
        self.bias_h2 = [random.uniform(-1, 1) for _ in range(self.hidden2_size)]

        # Hidden2 -> Hidden3
        self.weights_h2h3 = [[random.uniform(-1, 1) for _ in range(self.hidden2_size)] for _ in range(self.hidden3_size)]
        self.bias_h3 = [random.uniform(-1, 1) for _ in range(self.hidden3_size)]

        # Hidden3 -> Hidden4
        self.weights_h3h4 = [[random.uniform(-1, 1) for _ in range(self.hidden3_size)] for _ in range(self.hidden4_size)]
        self.bias_h4 = [random.uniform(-1, 1) for _ in range(self.hidden4_size)]

        # Hidden4 -> Hidden5
        self.weights_h4h5 = [[random.uniform(-1, 1) for _ in range(self.hidden4_size)] for _ in range(self.hidden5_size)]
        self.bias_h5 = [random.uniform(-1, 1) for _ in range(self.hidden5_size)]

        # Hidden5 -> Output
        self.weights_ho = [random.uniform(-1, 1) for _ in range(self.hidden5_size)]
        self.bias_o = random.uniform(-1, 1)

        self.learning_rate = 0.1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_deriv(self, x):
        sx = self.sigmoid(x)
        return sx * (1 - sx)

    def act(self, history_self, history_opponent):
        roundcounter = len(history_self)
        if roundcounter < 4:
            return self.COOPERATE

        inputs = [
            int(history_self[-3]),
            int(history_self[-2]),
            int(history_self[-1]),
            int(history_opponent[-3]),
            int(history_opponent[-2]),
            int(history_opponent[-1])
        ]

        # Vorwärtsdurchlauf: Input -> Hidden1
        hidden1 = []
        z1s = []
        for h in range(self.hidden1_size):
            z1 = sum(w * i for w, i in zip(self.weights_ih1[h], inputs)) + self.bias_h1[h]
            z1s.append(z1)
            hidden1.append(self.sigmoid(z1))

        # Hidden1 -> Hidden2
        hidden2 = []
        z2s = []
        for h in range(self.hidden2_size):
            z2 = sum(w * h1 for w, h1 in zip(self.weights_h1h2[h], hidden1)) + self.bias_h2[h]
            z2s.append(z2)
            hidden2.append(self.sigmoid(z2))

        # Hidden2 -> Hidden3
        hidden3 = []
        z3s = []
        for h in range(self.hidden3_size):
            z3 = sum(w * h2 for w, h2 in zip(self.weights_h2h3[h], hidden2)) + self.bias_h3[h]
            z3s.append(z3)
            hidden3.append(self.sigmoid(z3))

        # Hidden3 -> Hidden4
        hidden4 = []
        z4s = []
        for h in range(self.hidden4_size):
            z4 = sum(w * h3 for w, h3 in zip(self.weights_h3h4[h], hidden3)) + self.bias_h4[h]
            z4s.append(z4)
            hidden4.append(self.sigmoid(z4))

        # Hidden4 -> Hidden5
        hidden5 = []
        z5s = []
        for h in range(self.hidden5_size):
            z5 = sum(w * h4 for w, h4 in zip(self.weights_h4h5[h], hidden4)) + self.bias_h5[h]
            z5s.append(z5)
            hidden5.append(self.sigmoid(z5))

        # Hidden5 -> Output
        z_out = sum(w * h5 for w, h5 in zip(self.weights_ho, hidden5)) + self.bias_o
        output = self.sigmoid(z_out)

        action = self.COOPERATE if output >= 0.5 else self.DEFECT

        # Backpropagation (vereinfacht, nur für Demonstration)
        if roundcounter >= 4:
            target = int(history_opponent[-1])
            error = target - output
            d_output = error * self.sigmoid_deriv(z_out)

            # Hidden5 -> Output
            for h in range(self.hidden5_size):
                self.weights_ho[h] += self.learning_rate * d_output * hidden5[h]
            self.bias_o += self.learning_rate * d_output

            # Hidden5 Layer
            d_hidden5 = [d_output * self.weights_ho[h] * self.sigmoid_deriv(z5s[h]) for h in range(self.hidden5_size)]
            for h in range(self.hidden5_size):
                for h4 in range(self.hidden4_size):
                    self.weights_h4h5[h][h4] += self.learning_rate * d_hidden5[h] * hidden4[h4]
                self.bias_h5[h] += self.learning_rate * d_hidden5[h]

            # Hidden4 Layer
            d_hidden4 = [sum(d_hidden5[h5] * self.weights_h4h5[h5][h4] for h5 in range(self.hidden5_size)) * self.sigmoid_deriv(z4s[h4]) for h4 in range(self.hidden4_size)]
            for h4 in range(self.hidden4_size):
                for h3 in range(self.hidden3_size):
                    self.weights_h3h4[h4][h3] += self.learning_rate * d_hidden4[h4] * hidden3[h3]
                self.bias_h4[h4] += self.learning_rate * d_hidden4[h4]

            # Hidden3 Layer
            d_hidden3 = [sum(d_hidden4[h4] * self.weights_h3h4[h4][h3] for h4 in range(self.hidden4_size)) * self.sigmoid_deriv(z3s[h3]) for h3 in range(self.hidden3_size)]
            for h3 in range(self.hidden3_size):
                for h2 in range(self.hidden2_size):
                    self.weights_h2h3[h3][h2] += self.learning_rate * d_hidden3[h3] * hidden2[h2]
                self.bias_h3[h3] += self.learning_rate * d_hidden3[h3]

            # Hidden2 Layer
            d_hidden2 = [sum(d_hidden3[h3] * self.weights_h2h3[h3][h2] for h3 in range(self.hidden3_size)) * self.sigmoid_deriv(z2s[h2]) for h2 in range(self.hidden2_size)]
            for h2 in range(self.hidden2_size):
                for h1 in range(self.hidden1_size):
                    self.weights_h1h2[h2][h1] += self.learning_rate * d_hidden2[h2] * hidden1[h1]
                self.bias_h2[h2] += self.learning_rate * d_hidden2[h2]

            # Hidden1 Layer
            d_hidden1 = [sum(d_hidden2[h2] * self.weights_h1h2[h2][h1] for h2 in range(self.hidden2_size)) * self.sigmoid_deriv(z1s[h1]) for h1 in range(self.hidden1_size)]
            for h1 in range(self.hidden1_size):
                for i in range(self.input_size):
                    self.weights_ih1[h1][i] += self.learning_rate * d_hidden1[h1] * inputs[i]
                self.bias_h1[h1] += self.learning_rate * d_hidden1[h1]

        return action