# name="ram"
# marks=[]
# get_info():
#     name=input("Insert the name of th student"):
#     age=input("insert the age of the student"):
#     class=input("insert the class of the student":)
# get_result()

# MARKS=[]   #global variable 

# def get_marks():
#     no_of_subjects= int(input("Enter the number of subjects that you want:"))

#     for i in range(0, no_of_subjects,1):
#         value = int(input(f"Enter the mark obatained in{i+1}subject:"))   #local variable
#         MARKS.append(value)
# def get_info():
#     name= input("Enter the name of student")
#     Class= input("Enter the class of student")
#     roll = int(input("Enter the Roll number of students"))
#     global NAME 
#     global CLASS 
#     global ROLL 

#     NAME = name
#     CLASS = Class
#     ROLL= roll


# def get_result():
#     obtained_mark = 0
#     for i in range (len(MARKS)):       #len=length  (0,1,2,3) range(4)
#         obtained_mark = obtained_mark+MARKS[i]
#     print(f"student name-{NAME} of class {CLASS} with Roll no {ROLL} have obtained {obtained_mark}")

# get_info()    #calling function to execute the program
# get_marks()
# get_result()


'''
functiob=n to ake multiplication table 
get_ mul(n)
for i in range (11)
result=i*n

5*1=5
5*2=10

'''

x = int(input("Enter the number for the multiplication table:"))
y = int(input("Enter the number of rows for the multiplication table:"))

for i in range (1, y+1 ):
    result = x*i
    print (f"{x} * {i} ={result}")

else:
    if y> 10:
        print("The number of rows has been limited to 10.")