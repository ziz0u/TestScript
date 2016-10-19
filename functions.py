#!/usr/bin/env python
#
# constant  = a
# linear    = a(x)
# absolute  = |a|
# quadratic = a(x)2 = y = ax2 + bx + c
# inverse   = a/(x)
# cubic	  = a(x)2
# http://webapi.segupoliza.com/

import matplotlib.pyplot as plt

values=[]

def constant(a, f, t):
	for i in range(f, t):
		values.append(a)
	return values

def linear(a, f, t):
	for i in range(f, t):
		values.append(i*a)
	return values

def absolute(a, f, t):
	for i in range(f, t):
		values.append(abs(i))
	return values			

valuesx=[]
valuesy=[]
def quadratic(a, b, c, f, t):
	for i in range(f, t+1):
		x = i
		valuesx.append(x)
		y = a*i**2 + b*i + c
		valuesy.append(y)
	return valuesx, valuesy

print quadratic(1, 0, 0, -16, 16)
#print valuesx
#print valuesy

fig= plt.figure()
axes=fig.add_subplot(111)
#axes.plot([-3, -2, -1, 0, 1, 2, 3], [9, 4, 1, 0, 1, 4, 9])
axes.plot(quadratic(1, 0, 0, -16, 16))
plt.show()

#plt.plot(cuadratic(-4, -8, 8))
#plt.plot(absolute(1, -4, 5))
#plt.plot(constant(5, -4, 10))
#plt.plot(linear(3, 0, 15))
#plt.ylabel('some numbers')
#plt.show()

