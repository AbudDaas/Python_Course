#===========================================#
#===========>>Python Lists<<================#
#===========================================#

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, list1]
list3 = [True, False, list2]

# Length of the list
length = len(list3)
print(length, list3[-1][-1][1])
#===========================================
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#===========================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
#===========================================
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#=============================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#===============================================
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#===============================================
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#============================================
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#===========================================
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#===========================================
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)
#============================================
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#==========================================
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#===========================================
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#=============================================
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#===============================================
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#=================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#=================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
#===============================================
newlist = [x for x in range(10)]
print(newlist)
#================================================
newlist = [x for x in range(10) if x < 5]
print(newlist)
#=================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
#===============================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#================================================
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#=================================================
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#=================================================
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#=================================================
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#=================================================
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#================================================
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)