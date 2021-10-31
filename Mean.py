import csv

file = open("HW.csv", newline = "")
reader = csv.reader(file)
filedata = list(reader)
filedata.pop(0)
newData = []

for i in range(len(filedata)):
    num = filedata[i][1]
    newData.append(float(num))

n = len(newData)
total = 0

for i in newData:
    total = total + i

mean = total/n
print("Mean Is : " + str(mean))
