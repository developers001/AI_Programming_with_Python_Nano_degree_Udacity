
#let's visualise the function
import numpy as np
import matplotlib.pyplot as plt

#Todo Question 1: Read the following gradient descent function and describe what it is doing.
def gradient_descent(function, df, x_start, learning_rate=0.1, tol=0.00001, n_iter=1000, decay_rate =0 ):
    iters = 0 #iteration counter
    min_point = x_start
    X = [x_start]
    Y = [function(x_start)]
    #Todo in question 2
    while iters < n_iter:
        diff = - learning_rate * df(min_point) #important step. #Todo in question 2
        if np.all(np.abs(diff) <= tol):
            break
        min_point += diff #important step.
        iters += 1
        X.append(min_point)
        Y.append(function(min_point))
        print("Iteration",iters,"\nX value is",min_point, "\n Y value is",function(min_point)) #Print iterations

    return min_point, X, Y

#Question 1
#Todo Question 1: initialise x_start and run gradient descent to find the minimum point
function = lambda x: (x+5)**2
df = lambda x: 2*(x+5)  #Gradient of our function
x_start = None
ans, X, Y = gradient_descent(function, df, x_start)
print(ans)

#Plot the curve and the lines
x = np.linspace(-10,3,500)
plt.plot(x, function(x), 'b')
for i in range(0, len(X)):
    plt.plot(X[i:i+2], Y[i:i+2], 'ro-')
plt.show()



#Question 2
function = lambda x: x**4 - 5*(x**2) - 3*x
df = lambda x: 4*(x**3) - 10*x - 3

#Todo Question 2: Do the same with different parameters.
x_start = 2.4
ans, X, Y = gradient_descent(df, x_start, learning_rate=0.2)
print(ans)

x = np.linspace(-2.5,2.5,500)
#Plot the curve
plt.plot(x, function(x),'b')
for i in range(0,len(X)):
    plt.plot(X[i:i+2],Y[i:i+2],'ro-')
plt.show()

#Todo Question 2: Add Decay rate to the gradient descent function above and repeat
ans , X, Y = gradient_descent(df, x_start=-2, learning_rate=0.1,decay_rate=0.8)
print(ans)


#Question 3
#Generate some data
np.random.seed(42)
X = np.array(sorted(list(range(5))*20)) + np.random.normal(size=100, scale=0.5)
y = np.array(sorted(list(range(5))*20)) + np.random.normal(size=100, scale=0.25)

plt.clf()
plt.scatter(X, y, color='black')
plt.show()

#Implement the gradient descent function as above for linear regression for 2 variables.
def gradient_descent_reg(X, y, b_start=0.1, w_start=5, learning_rate=0.01, tol=0.00001, n_iter=1000):
    iters = 0 #iteration counter
    b = b_start
    w = w_start
    n = X.shape[0] #we have n data points
    while iters < n_iter:
        #calculate gradient of b and w
        b_gradient = np.sum(b+w*X-y)/n  # * here does element wise multiplication
        w_gradient = None #Todo
        diff_b = None  #Todo
        diff_w = None  #Todo
        if np.all(np.abs(diff_b) <= tol) and np.all(np.abs(diff_w) <= tol):
            break
        #Todo: update the values for w and b

        iters += 1

    return b, w

b,w = gradient_descent_reg(X, y)

plt.scatter(X, y, color='black')
plt.plot(X, w*X+b)
plt.show()
