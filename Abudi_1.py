#=========================================================================================================================#
#========================================================>Python Booleans<================================================#
#=========================================================================================================================#
print(9 < 10)      #========>>true
print(9 == 10)     #========>>false
print(9 > 10)      #========>>false
#======================================================
A = 50
Z = 30
if A < Z :
    print("Z is greater than A")    #==========>"A is greater than Z"
else:
    print("A is greater than Z")
#=======================================================
x = "Hello"
y = 15
print(bool(y))     #===========>true
print(bool(x))     #===========>true
#-=================================>>Etiketlerden birini koyarsanız,yanlış çıkacaktır.<<=======================================#
print(bool(False))   #========>>false
print(bool(None))    #========>>false
print(bool(0))       #========>>false
print(bool(""))      #========>>false
print(bool(()))      #========>>false
print(bool([]))      #========>>false
print(bool({}))      #========>>false
#======================================================
def myFunction() :
  return True           #========>True
print(myFunction())
#=====================================================
def myFunction() :
  return True
if myFunction():
  print("YES!") #======>YES
else:
  print("NO!")
#======================================================
x = 200 
print(isinstance(x,(int))     #===========>>true