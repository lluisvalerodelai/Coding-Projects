from math import e
import numpy as np

class Network:
    def __init__(self, num_per_layer, activation: str) -> None:
        self.npl = num_per_layer
        self.weights = []
        self.bias = []
        self.__create__()
        if activation.lower() == 'sigmoid':
            self.activation = self.__sigmoid
        elif activation.lower() == 'relu':
            self.activation = self.__relu
        else:
            self.activation = self.__activation


    def __create__(self):
        for i in range(1, len(self.npl)):
            self.weights.append(np.random.rand(self.npl[i - 1], self.npl[i]))

        for i in range(1, len(self.npl) - 1):
            self.bias.append(np.random.rand(1, self.npl[i]))
        self.bias.append(0)

    
    def Predict(self, X: list):

        X = np.array(X)

        output = np.dot(X, self.weights[0])

        for i in range(1, len(self.weights)):
            
            if i != len(self.weights) - 1:
                output = self.activation(np.dot(output, self.weights[i]) + self.bias[i])
            else:
                output = np.dot(output, self.weights[i])
            
            

        
        return output

    def __sigmoid(self, z):
        return 1/(1 + e**-z)
    
    def __relu(self, z, point = 0):
        return z * (z > point)

    def __activation(self, z):
        return z
    



n = Network((707, 200, 200, 20, 3), 'sigmoid')

X = np.random.rand(3, 707)

prediction = n.Predict(X)


print(prediction)

