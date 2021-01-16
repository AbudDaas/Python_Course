thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#=====================================
thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))
#================================
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#===================================
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#================================
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#============================
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#=============================
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#==============================
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#=============================
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#==========================
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#==============================
tuple1 = ("b", "w" , "z")
tuple2 = (5, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#==================================
fruits = ("orange", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#================================
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(9)
print(x)
#==================================
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
z = thistuple.index(8)
print(z)
#================================
