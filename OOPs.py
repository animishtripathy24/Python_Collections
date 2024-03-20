class Employee:
    #creating a constructor
    def __init__(self,gname,gsalary):
        self.name=gname
        self.salary=gsalary

#creating a object of Employee class
animish=Employee("Animish",1500000)
print(animish.name)
print(animish.salary)
