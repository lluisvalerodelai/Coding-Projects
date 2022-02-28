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
            
            
        
        def GradientDescent(self, X, Y, lr) -> list:

            losses = []
            
            for i in range(len(X)):
                for j in range(len(X[i])):
                    print(self.Error(Y, self.hypothesis(X)))
                    a.append(self.Error(Y, self.hypothesis(X)))

                    derivative_of_loss_WRT_theta = 2*(self.hypothesis(X)[i] - Y[i]) * X[i][j]

                    self.params[j] = self.params[j] - lr * derivative_of_loss_WRT_theta

            return losses
