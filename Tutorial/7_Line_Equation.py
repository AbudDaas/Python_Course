import matplotlib.pyplot as plt
import numpy as np

# Lines
testList0 =[(1, 8), (5, 6)] # Original Line
testList1 =[(0, 8), (4, 6)] # Shifted X-Axis
testList2 =[(1, 7), (5, 5)] # Shifted Y-Axis

crossLine = [(1,6),(3, 8)]
# Edges
edge1 = [(1, 8), (0, 8), (1, 7)]#, (1, 8)]
edge2 = [(5, 6), (4, 6), (5, 5), (5, 6)]

# coordinates
x_0 = [x[0] for x in testList0]
y_0 = [x[1] for x in testList0]

x_1 = [x[0] for x in testList1]
y_1 = [x[1] for x in testList1]

x_2 = [x[0] for x in testList2]
y_2 = [x[1] for x in testList2]

# draw Points
plt.scatter(x_0,y_0)
plt.scatter(x_1,y_1)
plt.scatter(x_2,y_2)
# plt.scatter(*zip(*testList2)) # scatter([x0,x1,...,xn], [y0,y1,...,yn]) --> zip

# plot Lines
plt.plot(x_0, y_0, 'b-', label='Original') # Blue
plt.plot(x_1, y_1, 'r-', label='X-Shift') # Red
plt.plot(x_2, y_2, 'y-', label='Y-Shift') # Gren
# plt.plot(*zip(*testList2), 'r-') # Red

plt.plot(*zip(*edge1), 'c')
plt.plot(*zip(*edge2), 'c')
plt.plot(*zip(*crossLine), 'rx--')

plt.title('Schematic diagram')
plt.xlabel('X-satır')
plt.ylabel('Y-satır')
plt.legend()
plt.grid()
plt.show()