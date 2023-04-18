import numpy as np
import matplotlib.pyplot as plt

def yFunction(x):
    return x ** 2
   # return np.sin(x)

def yDerivative(x):
    return 2 * x
   # return np.cos(x)
   

x = np.arange(-100,100,0.1)
y = yFunction(x)


currentPos = (80, yFunction(80))

learningRate = 0.001

for _ in range(1000):
    new_x = currentPos[0] - learningRate * yDerivative(currentPos[0])
    new_y = yFunction(new_x)
    currentPos = (new_x,new_y)

    
    plt.plot(x,y)
    plt.scatter(currentPos[0],currentPos[1],color = "red")
    plt.pause(0.001)
    plt.clf()
