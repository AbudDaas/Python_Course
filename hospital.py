# Empty list
hospital=[]

#-------------------
# Class Patient
#-------------------
class Patient:
    def __init__(self):
        # Empty Dictionary
        self.records = {}

    def add(self, name, id_n, wardNo, doctor):
        self.records['id_no'] = id_n
        self.records['ward_no'] = wardNo
        self.records['name'] = name
        self.records['doctor'] = doctor
        hospital.append(self.records)

    def display(self):
        return self.records

    def search(self):
        ch1 = int(input("Search By:\n 1.Name \n 2.Id \n 3.Ward number \n 4.Disease Type\n"))
        if ch1 == 1:
            name1 = input('Enter name to be searched')
            while self.records['name'] != name1:
                break
            return f" id : {self.records['id_no']} Name: {self.records['name']} Ward no: {self.records['ward_no']}"
    def delete(self,del_item):
        while del_item != self.records['id_no']:
            pass
        del self.records
#----------------------------------------------------
# Instance of the class
i = Patient()

while True:
    ch = int(input("""Enter Choice  
1.Admit new Patient 
2.Discharge Patient 
3.Display status of each ward
4.Search Record
5.Exit Portal
"""))
    if ch == 1:
        nname = str(input('Enter patient Name'))
        id_no = int(input('Enter id no'))
        ward_no = int(input('Enter ward no'))
        doc = str(input('Enter appointed doctor\'s name'))
        i.add(nname, id_no, ward_no, doc)
    elif ch == 2:
        n = int(input('Enter the id.no to be discharged'))
        i.delete(del_item=n)
        pass
    elif ch == 3:
        print(hospital)
    elif ch == 4:
        i.search()
    else:
        print('Enter correct choice')