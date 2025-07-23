name = "Mohamed"
age = 20
skills = ["Python", "Translating", "Communication"]
info = {"city": "Benisuef", "country": "Egypt"}

print(type(name))    
print(type(age))      
print(type(skills))   
print(type(info))     

skills.append("Machine Learning")
print(skills)

class Employee:
    title = "computer science student"
    
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def year_salary(self):
        return self.salary * 12

    @classmethod
    def get_company(cls):
        return cls.title

    @staticmethod
    def valid_salary(salary):
        return salary >= 6000

emp1 = Employee("Salem", "IT", 8000)
emp2 = Employee("farouk", "HR", 5500)

print(emp1.display_info())
print(emp2.display_info())

print("Employee Info:", emp1.display_info())
print("Yearly Salary:", emp1.year_salary())

print("Company Name:", Employee.get_company())

print("Is Salary Valid?", Employee.valid_salary(emp2.salary))
