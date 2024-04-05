import csv

list1 = []

with open('Movie_Id_Titles.csv','r', errors='ignore') as cs:
    creader = csv.reader(cs)
    next(creader)
    for line in creader:
        list1.append(line[1])
for i in list1[::10]:
    if("Monkey" in i):
        print("yes")
    else:
        pass