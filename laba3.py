import csv

with open('C:\\Users\\Анна\\Documents\\python\\exp.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)	


import csv
 
results = []
with open('C:\\Users\\Анна\\Documents\\python\\exp.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print(results)        