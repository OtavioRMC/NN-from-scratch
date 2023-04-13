# Training Neural Network Part 1
import numpy as np

def mseLoss(yTrue, yPred):
    # yTrue and yPred are numpy arrays of the same length.
    return ((yTrue - yPred)**2).mean()

yTrue = np.array([1,0,0,1])
yPred = np.array([0,0,0,0])

print(mseLoss(yTrue,yPred)) # 0.5

