from pylab import *

x = linspace(-8,8,201)
z = 5*exp(2j*x) + 7*exp(3j*x)

plot(x,abs(z),label='module')
plot(x,angle(z),label='argument')
legend()

show()
