# myList =["HELLO",True, 123,32.5,[1,"ram","hari",["window","mac"]]]
# print(myList[4][3][1])

# myList.append("Nep Tech Pal")
# print("myList")

# myList.insert(3,"Deepti")
# print(myList)

# myList[0]="hi"
# print(myList)

# myList.remove("hi")
# print(myList)

'''
Ask user for first number
Ask user for operator
Ask user for second number

if operator=="+"
    print(f"The sum of{num1}and{num2}is {num1+num2}")

'''

# num1= int(input("Enter the first number"))
# operator= input("Enter a operator")
# num2= int(input("Enter a second number"))

# if operator=="+":
#     print(f"The sum of{num1}and{num2}is {num1+num2}")
# elif operator=="-":
#     print(f"The subtraction of{num1}and{num2}is {num1-num2}")
# elif operator=="*":
#     print(f"The multiplication of{num1}and{num2}is {num1*num2}")
# elif operator=="/":
#     print(f"The division of{num1}and{num2}is {num1/num2}")
# else:
#     print(f"the sum is invalid")

'''
 Enter a users basic information
 '''

# name="Deepti Bhujel"
# age=18
# gender="Female"
# qualification="High school graduate"
# Phone_number =9806551296

# print(f"My name is {name}.I'm {age} years old. I'm a {gender} and I'm a {qualification}. You can contact me at {Phone_number}")


# for i in range(10):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range (3,10,2):
#     print(i)

for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print("")

for i in range(4):
    for j in range(i+1):
        print(j, end ="")
    print("")    

for i in range(4):
    for j in range(i+1):
        print(j,end="")
    print("")