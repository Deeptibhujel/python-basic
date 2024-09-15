
class Human:
    def __init__(self,name, gender, age):             #self is compulsory
        self.name = name
        self.gender = gender
        self.age =age

    def check_vote(self):
        if self.age> 18:
            print(f"{self.name} can vote")
        else:
            print(f"{self.name}can't vote")

    def __str__(self):
        return f"{self.name},{self.gender},{self.age}"
    

h1 = Human("xyz","male",20)          #object
h2= Human("abc","female",17)
h3 = Human("sita","female",19)

print(h1)
print(h2)
# h1.check_vote()
# h2.check_vote()
# h3.check_vote()

# print(h2.name, h2.gender, h2.age)

