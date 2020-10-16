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

myData = [["Last_name", "ave_salary", "sick_days"],
          ['Alexeev', '26000', '3'],
          ['Sidorenko', '40000', '14']]
 
myFile = open('C:\\Users\\Анна\\Documents\\python\\exp.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")