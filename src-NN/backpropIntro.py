# Backpropagation Basics

import numpy as np
import matplotlib.pyplot as plt


'''
 Weight(s) are randomly initialized
 Considering a training set:
 Single data input/output pair

 # Without Optimization
 Input: 1.5
 Desired Output: 0.5
 Random Weight: 0.8
 Output: 1.2

 To train or optmize a neural network is by changing the weights in such way 
 that output activation becomes corret.

 # With Optimization
Input: 1.5
Desired Output: 0.5
Random Weight: ?


'''
def actFunction(input,weight):
    output = input * weight
    return  output

def MSEloss(output,desired_out):
    return (output - desired_out)**2
'''
How should output change for error to decrease? 
--> How should W(weight) change for output to change in such a way that error decreases?
This process is called backpropagation.
'''

def derivMSEloss(outout,desired_out):
    return 2*(outout - desired_out)

def derivActFunction(input,weight):
    return input


# How should w change for output to change in such way that error decreases?

def chainRule(input,output,desired_out):
    dActFunction_dweight = derivActFunction(input,output)
    dMseLoss_dActFunction = derivMSEloss(output,desired_out)
    return dActFunction_dweight * dMseLoss_dActFunction

# Ploting MSEloss function

x = np.linspace(-1,1.5,num=100,endpoint=True)
y = MSEloss(x,0.5)

# Create a plot
plt.plot(x,y)

# Add labels
plt.xlabel('x')
plt.ylabel('MSE Loss')
plt.title("Mean Squared Error Function")

# Display the plot
plt.show()

''' 
Easy explanation for how backpropagation is done. Topics covered:
- gradient descent
- exploding gradients
- learning rate
- backpropagation
- cost functions
- optimization steps
'''