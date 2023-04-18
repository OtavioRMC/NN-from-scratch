import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def zFunction(x,y):
    return np.sin(5*x) * np.cos(5*y) / 5

def calculateGradient(x,y):
    return np.cos(5 *  x) * np.cos(5 * y), -np.sin(x * 5) * np.sin(5 * y)


x = np.arange(-1,1,0.05)
y = np.arange(-1,1,0.05)

x , y = np.meshgrid(x,y)

Z = zFunction(x,y)

current_pos = (0.7,0.4,zFunction(0.7,0.4))

learningRate = 0.01

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,Z,cmap="viridis")

for _ in range(1000):

  x_derivative, y_derivative = calculateGradient(current_pos[0],current_pos[1])
  x_new, y_new = current_pos[0] - learningRate * x_derivative,current_pos[1] - learningRate * y_derivative
  current_pos = x_new, y_new , zFunction(x_new,y_new)

  ax.scatter(current_pos[0],current_pos[1],current_pos[2],color="red")
  plt.pause(0.01)

plt.show()