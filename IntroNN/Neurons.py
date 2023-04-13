import numpy as np
#import matplotlib.pyplot as plt


# Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

## Plot Sigmoid Function using Matplotlib.
# x = np.linspace(-6,6,100)
# y = sigmoid(x)

# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('sigmoid(x)')
# plt.show()

class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias

    def feedForward(self,inputs):
        # Weight inputs, add bias, then use the actvation function
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)    

weights = np.array([0,1]) #w1 = 0, w2 = 1
bias = 4
neuron = Neuron(weights, bias)

x = np.array([2,3]) #x1 = 2, x2 = 3
print(neuron.feedForward(x))

