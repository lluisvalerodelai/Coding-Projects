import numpy as np

class LinearRegressionLib:



    class model:
        def __init__(self, featureShape):
            self.params = np.random.rand(featureShape[0] + 1, 1)

        def hypothesis(self, X):

            #because our hypothesis is hθ(xⁱ) = θ₀ + θ₁x₁ ... θₙxₙ, and we are multiplying them as matrices(θ Xⁱ),  they need to be of shapes nxm, mxn
            #currently, our data is a nxm matrix, where n is the number of rows we have in our dataset, and m is the number of features per row
            #because we are initially adding θ₀ and not multiplying it by anything, we can add a 1 in the zero'th index of all our rows, so that it becomes θ₀1 + θ₁x₁ ... θₙxₙ
            #this will allow us to get the dot product of our data (nxm) and our parameters transposed (mx1)
            #this will give us a n dimensional vector(nx1) which will be the hypothesis per row of our data

            X = np.insert(X, 0, 1, axis = 1)

            prediction = np.array(np.dot(X, self.params))

            return prediction


        def Error(self, Y, Yhat):
            assert len(Y) == len(Yhat)

            #this is just mean squared error, we are returning the sum of each prediction with its respective label squared

            return np.sum(np.square(Yhat - Y))
            
            
        
        def GradientDescent(self, X, Y, lr) -> list:

            #to know by how much to tweak our parameters, we need to find how much each parameter affects the final output
            #to do this, we can take the partial derivative of our error function w.r.t to each parameter using the chain rule,
            #this will tell us by how much each parameter affects the error/accuracy of our model, and we can update our parameters accrodingly


            losses = []
            
            for i in range(len(X)):
                for j in range(len(X[i])):
                    print(self.Error(Y, self.hypothesis(X)))
                    a.append(self.Error(Y, self.hypothesis(X)))

                    derivative_of_loss_WRT_theta = 2*(self.hypothesis(X)[i] - Y[i]) * X[i][j]

                    self.params[j] = self.params[j] - lr * derivative_of_loss_WRT_theta

            return losses









