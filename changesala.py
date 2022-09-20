class employe:
    company="micrp"
    salary=1000
    
    # def changesalary(self,sal):    --> dunder class method
    #     self.__class__.salary=sal
    
    @classmethod                      #decorator
    def changesalary(cls,sal):
        cls.salary=sal

    
e=employe()
print(e.salary)
e.changesalary(200)
print(e.salary)
print(employe.salary)