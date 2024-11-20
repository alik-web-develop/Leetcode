class House():
    def __init__(self,street,number,age):
        self.street = street
        self.number = number
        self.age = age
        self.year = 2024
    def build_year(self):
        return f"your house building a {self.year - self.age} year"
    def build(self):
        return f"your house street is {self.street} and your house number {self.number}"
    
house1 = House("хуёвая","52",2016)
print(f"your house info {house1.build()},  {house1.build_year()}")