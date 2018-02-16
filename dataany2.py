import csv
import operator
import os

name = raw_input()

myfile = name
o = open(myfile, 'rU')
mydata = csv.reader(o)


sortedlist = sorted(mydata, key=operator.itemgetter(1), reverse=True)

for row in sortedlist:
    #print(row)
    print(row[0], row[1], row[2], row[3], row[4])
   # if row+1[1]<row[1]:
   #      row[1]=temp
   #      row[1]=row+1[1]
   #      temp=row+1[1]
o.close()

print('Enter the name for the output file')
ofile = raw_input()

with open(ofile, 'wb') as csvfile:
    sortwriter = csv.writer(csvfile)
    sortwriter.writerow(sortedlist)
