import matplotlib.pyplot as plt
# List of [(x,y)]
#testList =[(0, 6), (1, 2), (2, 7), (3, 5), (4, 3), (5, 9)]

#x_ada = [x[0] for x in testList]
#y_ada = [x[1] for x in testList]

#plt.scatter(x_ada,y_ada)
#plt.scatter(*zip(*testList)) # scatter([x0,x1,...,xn], [y0,y1,...,yn]) --> zip
#plt.plot(x_ada, y_ada, 'ro') # Red
#plt.plot(x_ada, y_ada, 'b-') # Blue

#plt.title('Random Figure')
#plt.xlabel('X-Axis')
#plt.ylabel('Y-Axis')
#plt.grid()
#plt.show()

testList =[(7, 1), (7, 4),]

import matplotlib.pyplot as plt

x_ada = [x[0] for x in testList]
y_ada = [x[1] for x in testList]

plt.scatter(x_ada,y_ada)
plt.scatter(*zip(*testList)) # scatter([x0,x1,...,xn], [y0,y1,...,yn]) --> zip
plt.plot(x_ada, y_ada, 'ro') # Red
plt.plot(x_ada, y_ada, 'b-')

plt.title('Schematic diagram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.grid()
plt.show()