import numpy as np
from Neurons import Neuron



class NeuralNetwork:
    '''
      A Neural Network with:
      -2 iputs
      - a hiddlen layer with 2 neurons (h1,h2)
      - an output layer with 1 neuron (o1)
      Each Neuron has the same weights and bias:
      - w = [0,1]
      - b = 0    
    '''
    def __init__(self):
     weights = np.array([0,1])
     bias = 0

     # Neuron Class
     self.h1 = Neuron(weights,bias)
     self.h2 = Neuron(weights,bias)
     self.o1 = Neuron(weights,bias)

    def feedForward(self,x):
       out_h1 = self.h1.feedForward(x)
       out_h2 = self.h2.feedForward(x)
       # The Inputs for o1 are the outputs from h1 and h2.
       out_o1 = self.o1.feedForward(np.array([out_h1,out_h2]))   

       return out_o1

network = NeuralNetwork()
x = np.array([2,3])    
print(network.feedForward(x))