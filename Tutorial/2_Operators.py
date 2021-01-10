#===========================================#
#===========>>Python Operators<<============#
#===========================================#
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)        #same as 2*2*2*2*2
print(x // y)
#======================================
x = 5
x += 3
print(x)
#=====================================
x = 5
x -= 3
print(x)
#=====================================
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(x > 3 or x < 4)
#=====================================
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))
#=====================================
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
#=====================================
print(x is not z)
print(x is not z)
print(x != y)
#====================================
x = ["apple", "banana"]
print("banana" in x)
#====================================
x = ["apple", "banana"]
print("pineapple" not in x)
#===================================