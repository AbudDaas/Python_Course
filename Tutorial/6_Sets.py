thisset = {"apple", "banana", "cherry"}
print(thisset)
#=======================
thisset = {"apple", "banana", "cherry", "apple", "cherry"}
print(thisset)
#============================
thisset = {"apple", "banana", "cherry", "apple"}
print(len(thisset))
#==================================
set1 = {"cherry", "banana", "apple"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#=====================================
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#====================================
myset = {"apple", "banana", "cherry"}
print(type(myset))
#=====================================
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#===================================
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#===================================
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#=====================================
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#==================================
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#=========================================
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#=====================================
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#==================================
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#==============================
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#===============================
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#====================================
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#====================================
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#==================================
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#=============================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#==================================
# x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#================================================