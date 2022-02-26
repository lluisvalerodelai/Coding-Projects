import numpy as np


class LinearRegressionLib:



    class model:
        def __init__(self, featureShape):
            self.params = np.zeros((featureShape[0] + 1, 1))
        

        def hypothesis(self, X, returnMean = False):
            

            #because our hypothesis is hθ(xⁱ) = θ₀ + θ₁x₁ ... θₙxₙ, and we are multiplying them as matrices(θ Xⁱ),  they need to be of shapes nxm, mxn
            #currently, our data is a nxm matrix, where n is the number of rows we have in our dataset, and m is the number of features per row
            #because we are initially adding θ₀ and not multiplying it by anything, we can add a 1 in the zero'th index of all our rows, so that it becomes θ₀1 + θ₁x₁ ... θₙxₙ
            #this will allow us to get the dot product of our data (nxm) and our parameters transposed (mx1)
            #this will give us a n dimensional vector(nx1) which will be the hypothesis per row of our data
               
            X = np.insert(X, 0, 1, axis = 1)

            prediction = np.array(np.dot(X, self.params))



            if returnMean:
                return prediction.mean()
            else:
                return np.reshape(prediction, (-1, 1))
        
        def Error(self, Y, Yhat, ErrorPerExample = False):
            assert len(Y) == len(Yhat)
            
            if ErrorPerExample:
                error = []
                for i in range(len(Y)):
                    error.append(int((Y[i] - Yhat[i])**2))
                return error
            else:
                Error = 0
                for i in range(len(Y)):
                    Error += (Y[i] - Yhat[i])**2
                
                return Error
        
        def GradientDescent(self, X, Yhat, Y, lr, epochs, printInfo = True):

            errors = [self.Error(Y, Yhat)]
            
            if printInfo:


                for epoch in range(epochs):
                    
                    print(f'------------------ epoch {epoch} ------------------')

                    partial_derivatives_per_training_example = []

                    for i in range(len(X)):

                        #go through each training example and compute the partial derivative of each of our parameters with respect to the loss function
                        #we want to calculate the partial derivative of parameter θₙ w.r.t Error(), so we need to use the chain rule
                        #using the chain rule, we have to multiply the partial derivative of θₙ w.r.t hypothesis() and the partial derivative of hypothesis() w.r.t Error()
                        #to calculate the partial derivative of θₙ w.r.t Error(), we see that it is just xₙ, because our hypothesis is θ₀ + θ₁x₁ ... θₙxₙ


                        #so our first partial derivatives are just the feature vector
                        p_derivs = [1]

                        for item in X[i]:
                            p_derivs.append(int(item))

                        
                        #we then multiply each of those derivatives with the derivative of hypothesis() w.r.t Error()
                        #this is just 2(ŷ - y) because error is (ŷ - y)^2
                        for j in range(len(p_derivs)):
                            p_derivs[j] = float(p_derivs[j] * (2*((Yhat[i] - Y[i])**2)))
                        print(f'------------------ epoch {epoch} ------------------')
                        print(f'partial derivatives: {p_derivs}')
                        
                        #we then add this to the list of derivatives

                        partial_derivatives_per_training_example.append(p_derivs)
                    
                    
                    
                    #now we have a list with how much to update our parameters per training example
                    #now we can take the average of each column to know by how much to update our parameters
                    
                    avgs = np.array(partial_derivatives_per_training_example).mean(axis = 0)

                    new_params = []

                    for i in range(len(avgs)):
                        new_params.append(self.params[i] - (lr * avgs[i]))
                    
                    self.params = np.array(new_params)
                    

                    errors.append(self.Error(Y, Yhat))

                
            return errors

        #this function is extremely slow, we have a triple nested loop, and the middle loop if potentially massive
        #to optimize, I can split up X into small batches, and repeat this process per batch

        
#broken, gradient descent is not working, still trying to find out why
