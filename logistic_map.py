import matplotlib.pyplot as plt
import numpy as np

def logistic_eqn(rate,x):
    return rate * x * (1 - x)

def logistic_eqn_2(rate,x):
    return rate * x * (1 - x**2)

def logistic_eqn_3(rate,x):
    return rate * x * (1 - x**3)

def logistic_eqn_4(rate,x):
    return rate * x * ((1 - x)**2)

def logistic_eqn_5(rate,x):
    return rate * x * ((1 - x)**3)


# Creates 50 (default) evenly spaced numbers between interval of 0 to 1
x =  np.linspace(0,1)
# Creates y values for logistic eqn with rate of 2 and x values between 0 and 1
y = logistic_eqn_5(2,x)

# Creates a figure containing a single axes
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('xo')
ax.set_ylabel('xn')
ax.set_title('r = 2')
plt.show()
# Creates y values for logistic eqn with rate of 3 and x values between 0 and 1
y = logistic_eqn_5(3,x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('xo')
ax.set_ylabel('xn')
ax.set_title('r=3')
plt.show()

# Creates an array n rate values between
n = 1000
r = np.linspace(0,4,n)
iterations = 500
# x = 0.5 * np.ones(n)
x = 0.5
print(x)

fig, ax1 = plt.subplots()
for i in range(iterations):
    x = logistic_eqn_5(r,x)
    ax1.plot(r,x)
ax1.set_title('Bifurcation Diagram')
ax1.set_xlabel('Rate')
ax1.set_ylabel('Equilibrium Population')
ax1.legend()
plt.show()

