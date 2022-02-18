#still not working, i think i got gradient descent right but i still cant get it to set both thetas to the correct values, but i havent double checked it yet so its probably very obvious



import numpy as np

data = {
        'House_Size'   : np.array([[1000, 2000, 3000, 5000, 7000, 8000, 9000, 10000, 13000]]),
        'House_prices' : np.array([[100, 200,  300,  500,  700,  800, 1000, 1400, 1700]])
        }

    

class Model:
    def __init__(self, params):
        self.params = params
        self.theta1 = params[0]
        self.theta2 = params[1]

    
    def hypothesis(self, x):
        new_x = []
        for i in x:
            new_x.append([1, i])

        hypothesis = []
        for i in range(len(new_x)):
            hypothesis.append((self.params[0] * new_x[i][0]) + self.params[1] * new_x[i][1])
        
        return np.array(hypothesis).T
    
    def cost(self, Y_hat, Y):
        assert len(Y_hat) == len(Y), 'not same length'
        summ = []
        for i in range(len(Y_hat)):
            summ.append((Y_hat[i] - Y[i])**2)
        summ = sum(summ)

        self.error = (1/(2*len(Y))) * summ
        return self.error
    
    def train(self, lr, guesses, y, x):
        summ = []

        for i in range(len(guesses)):
                summ.append((guesses[i] - y[i])**2)
        sum1 = sum(summ)

        self.theta1 = self.theta1 - lr * (1/len(guesses)) * sum1
        self.theta2 = self.theta2 - lr * (1/len(guesses)) * (summ * x)
        
        
    
m = Model([10, 10])
m_hypothesis = m.hypothesis(data['House_Size'])
print(f'hypothesis is {m_hypothesis}')
print('cost is: ' + str(m.cost(m_hypothesis, data['House_prices'].T)))

for i in range(10):
    m.train(0.01, m_hypothesis, data['House_prices'].T, data['House_Size'].T)

print(m.theta1, m.theta2)

