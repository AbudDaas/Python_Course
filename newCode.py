#----------------------------------------------------------------------------------------------------------------#
#--------------------------------------------->#paython strings<-------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#
for x in"bomba":
    print(x)
#--------------------------------
txt = "The best things in life are free!"
print("free" in txt)
#---------------------------
a = "korona"
print(a[1:5]) 
#--------------------------------
txt = "Cheetah in a wild animal"
if "cheetah" in txt:
 print("yes,them 'wild animals'")
#--------------------------------------
txt = "The best things in life are free!"
print("expensive" not in txt)
#--------------------------------------------
a = "Hello, World!"
print(a.upper())
#--------------------------------------------
a = "Hello, World!"
print(a.lower())
#--------------------------------------------
a ="korona, vayrus"
print(a.replace("k", "D"))
#--------------------------------------------
a = "my, name"
print(a.split(","))
#--------------------------------------------
age = 13
txt = "My name is John, and I am {}"
print(txt.format(age))
#--------------------------------------------
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#-------------------------------------------
