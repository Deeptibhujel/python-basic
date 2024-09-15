
class Category:
    def __init__ ( self,  category, fuel_type):
        self.category = category
        self.fuel_type = fuel_type
    def __str__(self):
        return f"{self.category},{self.fuel_type}"

c1 = Category ("car","petrol")
c2 = Category("truck","disel")
    
print(c1)
print(c2)