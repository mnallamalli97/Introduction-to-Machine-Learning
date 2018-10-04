#function to print name and title
def printNameTitle(name="N/A", title="N/A"):
    print(employeeDictionary["name"], employeeDictionary["title"])

name = []
age = []
salary = []
title = []

#allows user to input 10 employees into dictionary
i = 1
while i  <= 10:
    #input name
    name.append(input(print("enter name of emp: ")))

    #input age
    age.append(int(input(print("enter age of emp: "))))

    #input salary
    salary.append(int(input(print("enter salary of emp: "))))

    #input title
    title.append(input(print("enter title of emp: ")))

    #increment counter to indicate new employee
    i+=1


#write to dictionary
employeeDictionary = {"name": name, "age": age, "salary": salary, "title": title}

#write dictionary to file
try:
    fh = open('employees.txt', 'a')
except IOError:
    print("File not found.")

#write the whole dictionary to file at once (rather than individually)
fh.write(str(employeeDictionary))

try:
    for j in range(0,10):
        if employeeDictionary["salary"][j] > 60000:
            print("{0} is/are rich".format(employeeDictionary["name"][j]))
        else:
            print("{0} is/are poor".format(employeeDictionary["name"][j]))
except Exception as e:
    print("The exception is {0}".format(e))

