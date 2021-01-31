import matplotlib.pyplot as plt 

# Line defined with Two points p1, p2
p1 = (0, 1)
p2 = (3, 4)
Line = [p1, p2]

x = range(0,10) # [0, 1 ,..., 9]
y = []

# Line defined with one point and slope (m)
(x0,y0) = (0,1)
m = 0.5
a = m
b = 1
c = y0 - m * x0

[y.append((a*xi+c)/b) for xi in x] # y = (a * x + c)/b

# Center
Center = (4, 3)

# draw figure
plt.figure(num='Line')
plt.title('Line Equation')
# Center
plt.scatter(Center[0], Center[1], color='blue', label='Center')
# Line m, (x0, y0)
plt.plot(x,y,'gx--', label='Point and Slope (m)')
# Line []p1, p2
plt.plot(*zip(*Line),'ro--', label='Tow Points')

plt.xlabel('X-satır')
plt.ylabel('Y-satır')

plt.legend()
plt.grid()
plt.show()