import numpy as np

class model:
    def __init__(self, data_shape):
        self.params = np.random.rand(data_shape[0] + 1, 1)
    
    def hypothesis(self, data):
 
        #this hypothesis takes in a single feature vector

        #because our hypothesis is hθ(xⁱ) = θ₀ + θ₁x₁ ... θₙxₙ, and we are multiplying them as matrices(θ Xⁱ),  they need to be of shapes nxm, mxn
        #currently, our parameters are a vector (10, 1) and our features are a vector (9, 1).
        #because we are initially adding θ₀ and not multiplying it by anything, we can add a 1 in the zero'th index of our data, so that it becomes θ₀1 + θ₁x₁ ... θₙxₙ
        #this will also make our shapes nxm, mxn

        #insert the 1 at (xⁱ₀)
        data = np.insert(data, 0, 1, axis = 0)

        assert data.shape == self.params.shape, f'data shape is {data.shape} and parameters shape is {self.params.shape}'

        #multiply the vectors to get our hypothesis
        return np.round(np.dot(self.params.T, data), 2)
    
    def table_hypothesis(self, data):
        
        #this hypothesis takes in a row of feature vectors

        #first go through every feature vector and add x0 == 1
        new_data = np.insert(data,0, np.ones(data.shape[0], int), axis = 1)

        

        return np.round(np.dot(new_data, self.params), 2)

    def meanSquaredError(self, Y_hat, Y):
        mse_list = []
        for i in Y_hat:
            print(i)
            mse_list.append(np.round(np.mean((Y_hat - Y)**2)))
        return np.array(mse_list)

    
    def gradientDescent(self, lr, data, Y, iterations):

        #something broke when I did this, suddenly I have a -infinity somewhere, still debugging
        
        for j in range(iterations):
            for i in range(len(self.params) - 1):
                avg = np.mean(data[:, i])
                self.params[i] = self.params[i] - lr * (1/len(self.params)) * (sum(self.meanSquaredError(self.table_hypothesis(data), Y))) * avg
        

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

data.resize(9, 1)

data1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14, 15, 16, 17, 18],
                  [19, 20, 21, 22, 23, 24, 25, 27, 28],
                  [29, 30, 31, 32, 33, 34, 35, 36, 37]], dtype=float)


data1_Y = np.array([100, 200, 300, 400], dtype=float)

m = model(data.shape)

Y_hat = m.table_hypothesis(data1)


print(m.meanSquaredError(Y_hat, data1))

m.gradientDescent(1, data1, data1_Y, 1)

