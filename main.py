equipment = {
    "Microscope" : 5,
    "Beaker" : 20,
    "Flask" : 15,
    "thermometer" : 8
}

def show_equipment ():
    for item in equipment:
        print( item,"-",equipment[item], "available")
def borrow_equipment():
    student= input("Enter student name: ")
    item = input("Enter equipment name: ").lower()

    for name in equipment
        if name.lower() == item:
            if equipment[name] > 0:
                equipment[name]-= 1
                loans.append([student,name])

Output ("Equipment borrowed succesfully:")
    

