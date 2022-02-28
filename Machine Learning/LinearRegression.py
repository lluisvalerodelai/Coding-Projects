import numpy as np


class LinearRegressionLib:



    class model:
        def __init__(self, featureShape):
            self.params = np.random.rand(featureShape[0] + 1, 1)

        def hypothesis(self, X):

            X = np.insert(X, 0, 1, axis = 1)

            prediction = np.array(np.dot(X, self.params))

            return prediction


        def Error(self, Y, Yhat):
            assert len(Y) == len(Yhat)

            return np.sum(np.square(Yhat - Y))
            
            
        
        def GradientDescent(self, X, Yhat, Y, lr, epochs):

            losses = []

            for i in range(len(X)):
                for j in range(len(X[i])):
                    derivative_of_loss_WRT_theta = 2*(Yhat[i] - Y[i]) * X[i][j]

                    print(derivative_of_loss_WRT_theta)

                    self.params[j] = self.params[j] - lr * derivative_of_loss_WRT_theta
