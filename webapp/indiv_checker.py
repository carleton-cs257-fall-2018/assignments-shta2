import csv 

indivs = set([])
double = 0
lineNum = 0
csv_file = open('/Accounts/butterfieldp/Desktop/cs257/assignments-shta2/webapp/individual_donors.csv', encoding='utf-8')
reader = csv.reader(csv_file)


for row in reader:
    if(row[0] in indivs):
        double += 1
    indivs.add(row[0])
    lineNum += 1
    if lineNum % 200000 == 0:
        print(lineNum/200000)
csv_file.close()
print(lineNum)
print(double)