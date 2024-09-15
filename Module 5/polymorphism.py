
class Calculator:
   
    def calculate (self,x,y):
        return self.x +self.y
    
class Multiplication (Calculator):
   
    def calculate (self,x):
        return x * 10
    
class Addition( Calculator):
    
    def calculate (self,x,y,z):
        return x + y + z
    
m1 = Multiplication()
x = m1.calculate(10)
print (x)

a1 = Addition()
y= a1.calculate(10,20,30)
print(y)
