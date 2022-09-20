class employe():
    company="google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"welcome {self.name}") 

    def getsalary(self,sign):
        print(f"salarry is {self.salary} in {self.company} \n{sign}")
a=employe("atharv",100000)
# a.salary=100
# a.getsalary("atharv")      


