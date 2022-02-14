import pandas as pd
import matplotlib.pyplot as plt
data = {'House_Size':[100, 200, 220, 300, 700, 800],
        'price' : [100000, 120000, 130000, 160000, 300000, 400000]}

#M is the size of the dataset
M = len(data['House_Size'])
plt.plot(data['House_Size'], data['price'])
#plt.show()

class model:
    def __init__(self, theta1, theta2):
        self.theta1 = theta1
        self.theta2 = theta2
        

    
    def hypothesis(self, x):
        return self.theta1 + (self.theta2 * x)
    
    def MeanSquaredError(self, x, y):
        mae = 0
        summ = 0
        
        for i in range(len(x)):
            summ += (self.hypothesis(x[i]) - y[i])**2
        
        mae = (1/2*len(x))
        return mae
    
    def gradientDescent(self, learning_rate, x, y):
        

        newTheta1 = self.theta1 - learning_rate * (1/M * (self.MeanSquaredError(x, y)))
        newTheta2 = self.theta2 - learning_rate * (1/M * (self.MeanSquaredError(x, y)))

        self.theta1 = newTheta1
        self.theta2 = newTheta2

    def getmodel(self):
        return f'equation is {self.theta1} + {self.theta2} + x'
modell = model(0, 0)

print(modell.hypothesis(data['House_Size']))

for i in range(100):
    modell.gradientDescent(1, data['House_Size'], y = data['price'])

print(modell.getmodel())

