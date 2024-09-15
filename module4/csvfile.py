
import csv

# with open (" data, csv",'w') as file:
#     file.write ("ram, 10, 24")

# print("writing success)


#csv wrirter
student =[
    {"name":"xyz","Class":12, "roll":47},
    {"roll":20, "name":"ram","Class":11},
    {"name":"D",'Class':4,"roll":'5'}
    ]

with open ('data.csv','w') as file:
    filedname =['name','Class', 'roll']
    writer = csv. DictWriter(file, fieldnames = filedname)     
    writer.writeheader()
    writer.writerows(student)


with open('data.csv','r')as file:
    reader = csv.DictReader (file,delimiter= ",")      #delimeter is ,
    line_count=0            #not necessary
    for row in reader:
        print(row.get('Class'))