
name = input("Enter a student's name:")
Class = input ("Enter a class: ")
roll = int(input("Enter the roll number:"))

with open (" myfile.txt","w") as file:
    file.write(name)
    file.write (Class)
    file.write (str(roll)) 

print ("writing success!!!")

with open (" myfile.txt","r") as file:
    name= file. read()
    Class = file. read()
    roll = file. read()

print (name)
print(Class)
print(roll)




