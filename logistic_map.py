import matplotlib.pyplot as plt
import numpy as np

# assume x between 0 and 1
def logistic_eqn(rate,x):
    return rate * x * (1 - x)

def logistic_eqn_2(rate,x):
    return rate * x * (1 - x**2)

def logistic_eqn_3(rate,x):
    return rate * x * (1 - x**3)


# Double the penalty
def logistic_eqn_power(rate,x,n):
    return rate * x * ((1 - x)**n)

# Creates 50 (default) evenly spaced numbers between interval of 0 to 1
x =  np.linspace(0,1)
# Creates y values for logistic eqn with rate of 2 and x values between 0 and 1
y = logistic_eqn(2,x)

# Creates a figure containing a single axes
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('xo')
ax.set_ylabel('xn')
ax.set_title('r = 2')
plt.show()
# Creates y values for logistic eqn with rate of 3 and x values between 0 and 1
y = logistic_eqn(3,x)

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

fig, ax = plt.subplots()
for i in range(iterations):
    x = logistic_eqn(r,x)
    ax.plot(r,x)
ax.set_title('Bifurcation Diagram')
ax.set_xlabel('Rate')
ax.set_ylabel('Equilibrium Population')
ax.legend()
plt.show()

# fig, ax = plt.subplots()
# for i in range(1,10):
#     x = logistic_eqn_power(r,x,i)
#     ax.plot(r,x)
# ax.set_title('(1-x)^n')
# ax.set_xlabel('xo')
# ax.set_ylabel('xn')
# plt.show()

fig, ax = plt.subplots()
x = np.linspace(0,1)
for i in range(1,100):
    y = logistic_eqn_power(2,x,i/10)
    ax.plot(x,y)
ax.set_title('(1-x)^n')
ax.set_xlabel('xo')
ax.set_ylabel('xn')
plt.show()