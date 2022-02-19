import numpy as np

class model:
    def __init__(self, data_shape):
        self.params = np.random.rand(data_shape[0] + 1, 1)
    
    def hypothesis(self, data):
        
        #because our hypothesis is hθ(xⁱ) = θ₀ + θ₁x₁ ... θₙxₙ, and we are multiplying them as matrices(θ Xⁱ),  they need to be of shapes nxm, mxn
        #currently, our parameters are a vector (10, 1) and our features are a vector (9, 1).
        #because we are initially adding θ₀ and not multiplying it by anything, we can add a 1 in the zero'th index of our data, so that it becomes θ₀1 + θ₁x₁ ... θₙxₙ
        #this will also make our shapes nxm, mxn

        #insert the 1 at (xⁱ₀)
        data = np.insert(data, 0, 1, axis = 0)

        assert data.shape == self.params.shape, f'data shape is {data.shape} and parameters shape is {self.params.shape}'

        #multiply the vectors to get our hypothesis
        return np.dot(self.params.T, data)

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

data.resize(9, 1)

m = model(data.shape)



print(m.hypothesis(data))


