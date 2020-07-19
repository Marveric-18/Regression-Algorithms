# Simple Linear Regression
#### using Means Squarred Formula
## Linear regression is one of the most commonly used predictive modelling techniques. 

> It establishes a relationship between dependent variable (Y) and one or more independent variables (X) 
> best fit =  straight line (also known as a regression line).



### **y = c + m*x**
where
- y = estimated dependent score,
- c = constant,
- m = regression coefficient, and
- x = independent variable.

--------------------------------------------
#### Y is Dependent Varible
#### X is Independent Varible / Predictores
--------------------------------------------
Cost Function

#### C = (1/2n) * SIGMA(1-n)[(Yi - y) ** 2]
--------------------------------------------
Mean Squared Formula / Error Function / 
E = summation of ei**2

ei = (yi - Y)**2          Where Y= mean of y

Hence 	E = 1/n * SIGMA(1ton)[( yi- Y )**2 ]

#### E = 1/n * SIGMA(1ton)[( yi- (m*xi + c) )**2 ]
--------------------------------------------
Reducing the Error Function will get
Loss Function

darivation with respoect to m

#### dm = 1/n * SIGMA(1ton)[2( yi - (m*xi + c) ) * (-xi) ]
Hence
#### dm = -2/n * SIGMA(1ton)[( yi - Y ) * xi ]
--------------------------------------------
darivation with respoect to c

#### dm = 1/n * SIGMA(1ton)[2( yi - (m*xi + c) ) ]
Hence
#### dm = 2/n * SIGMA(1ton)[( yi - Y ) ]
--------------------------------------------
