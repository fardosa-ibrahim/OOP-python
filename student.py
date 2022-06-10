class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,country,age) :
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def greet(self):
        return f"Hello {self.first_name} {self.last_name} welcome to {self.school} how is {self.country}"
        

    def inituals(self):
        return f"Hello your inituals are {self.first_name[0]}{self.last_name[0]}"


    def birth_year(self):
        year_of_birth=2022-self.age
        return f"your age is {year_of_birth}"





        
        