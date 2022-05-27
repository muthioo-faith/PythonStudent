class Student:
     school = "Machakos Girls"
     def __init__(self,country,firstname,secondname,age):
        self.firstname = firstname
        self.country = country
        self.secondname = secondname
        self.age = age
     def full_name (self):

         return f"Hi {self.firstname} {self.secondname} How is {self.country}"
     def year_of_birth (self):  
         year=2022 - self.age
         return f"Hi {self.firstname} {self.secondname} How is {self.country} you were born in {year}"
     def initials (self):
         return f"Hi {self.firstname} {self.secondname} How is {self.country} your initials {self.firstname[0]} {self.secondname[0]}"