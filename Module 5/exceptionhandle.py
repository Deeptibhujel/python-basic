
a= int( input("Enter a number"))
b= int(input("Enter a second number"))

try:
    ans= a/b
    print(ans)
except Exception as e:
    print(e)

finally:
    print("Hello World")