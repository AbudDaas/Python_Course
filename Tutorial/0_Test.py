import matplotlib.pyplot as plt
import numpy as np

testList0=[(5, 6), (7, 8)]
testList1=[(5, 6), (6, 8)]

(x_0,y0) = (0,1)
m = 0.5
a = m
b = 1
c = y0 - m * x_0

Center = (5, 6)

x_0 = [x[0] for x in testList0]
y_0 = [x[1] for x in testList0]

x_1 = [x[0] for x in testList1]
y_1 = [x[1] for x in testList1]

plt.scatter(x_0,y_0)
plt.scatter(x_1,y_1)

plt.scatter(Center[0], Center[1], color='red', label='Center')

plt.plot(x_0, y_0, 'bx-', label='testList0') 
plt.plot(x_1, y_1, 'rx--', label='x-shift')

plt.title('Schematic diagram')
plt.xlabel('X-satır')
plt.ylabel('Y-satır')
plt.legend()
plt.grid()
plt.show()