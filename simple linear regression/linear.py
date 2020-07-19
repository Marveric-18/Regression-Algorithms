import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os

'''
--------------------------------------------
Simple Linear Regression
--------------------------------------------
Best Fit Line
y = m * x + c
--------------------------------------------
Y is Dependent Varible
X is Independent Varible / Predictores
--------------------------------------------
Cost Function

C = (1/2n) * SIGMA(1-n)[(Yi - y) ** 2]
--------------------------------------------
Mean Squared Formula / Error Function / 
E = summation of ei**2

ei = (yi - Y)**2          Where Y= mean of y

Hence 	E = 1/n * SIGMA(1ton)[( yi- Y )**2 ]

		E = 1/n * SIGMA(1ton)[( yi- (m*xi + c) )**2 ]
--------------------------------------------
Reducing the Error Function will get
Loss Function

darivation with respoect to m

dm = 1/n * SIGMA(1ton)[2( yi - (m*xi + c) ) * (-xi) ]
Hence
dm = -2/n * SIGMA(1ton)[( yi - Y ) * xi ]
--------------------------------------------
darivation with respoect to c

dm = 1/n * SIGMA(1ton)[2( yi - (m*xi + c) ) ]
Hence
dm = 2/n * SIGMA(1ton)[( yi - Y ) ]
--------------------------------------------
'''



#Reading data from database
dataframe = pd.read_csv('Salary.csv') 

#converting dataframes into arrays
y = np.array(dataframe['Salary'])
x = np.array(dataframe['YearsExperience'])

#cost function
def cost(slope, constant ,x ,y, n):
    return (.5/n) * np.sum(np.square(linear_formula(slope, constant, x)-y))

#y = m * x + c
def linear_formula(slope, constant, x):
	Y = slope * x + constant
	return Y

#loss function
def loss_function(slope, constant, n, x, y):
	Y_pred = linear_formula(slope, constant, x)
	dm = (-2/n) * sum(x * (y - Y_pred))
	dc = (-2/n) * sum(y - Y_pred) 
	return dm, dc

#gradient descent 
def gradient_descent(slope, constant, x, y, n, learning_rate, epochs= None):
	if epochs is None:
		epochs = 1000

	for epoch in range(epochs):
		print("epoch: {}".format(epoch))
		print("Cost : {}".format(cost(slope, constant, x, y, n)))
		print("------------------")
		D_m, D_c = loss_function(slope, constant, n , x, y)
		new_slope 		= slope - learning_rate * D_m
		new_constant 	= constant - learning_rate * D_c
		slope = new_slope
		constant = new_constant
		
	return new_slope, new_constant
		

#Simple Linear Regression

#initialize inputs
n = float(len(x))
slope = 0
constant = 0
learning_rate = 0.0001

# calling gradient_descent which will generate new_slope and new_constant
new_slope, new_constant =  gradient_descent(slope, constant, x, y, n, learning_rate, epochs= None)

print("------------------")
print(new_slope, new_constant)


#plotting the line and scatter graph
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  
    plt.plot(x, y)  

plt.scatter(x, y, c="red", alpha=0.5)
graph(linear_formula(new_slope, new_constant, x), range( 0,15))
plt.title('Scatter plot pythonspot.com')
plt.xlabel('Years Experience')
plt.ylabel('Salary')
plt.show()

#find new_Y according to our predictions
def find_new_Y(new_X, new_slope, new_constant):
	new_Y = linear_formula(new_slope, new_constant, new_X)
	return new_Y

print(find_new_Y(3.9, new_slope, new_constant))
print("------------------")

