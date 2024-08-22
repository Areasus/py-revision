# class Employee:
#     def __init__(self,eid,name,post,salary):
#         self.eid=eid
#         self.name = name
#         self.post = post
#         self.salary = salary
    
#     def __str__(self):
#         return f"Eid:{self.eid},name:{self.name}"
    
#     def postSalary(self):
#         return f"Post:{self.post},Salary:{self.salary:.2f}"
    
# e1 = Employee(1,"santosh","SE",123456)
# print(e1)
# print(e1.postSalary())

class Person:
    def __init__(self,eid,name):
        self.eid=eid
        self.name = name
    
    def __str__(self):
        return f"Eid:{self.eid},name:{self.name}"
    
class Employee(Person):
    def __init__(self,eid,name,post,salary):
       super().__init__(eid,name)
       self.post = post
       self.salary = salary
    
    def __str__(self):
        return super().__str__() + f" Post:{self.post},Salary:{self.salary:.2f}"
    
e1 = Employee(1,"santosh","SE",123.456)
print(e1)