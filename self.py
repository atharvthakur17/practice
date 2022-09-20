class employe():
    company="google"
    def getsalary(self,sign):
        print(f"salarry is {self.salary} in {self.company} \n{sign}")
    @staticmethod
    def greet():
        print("hello , welcome")


a=employe()
a.salary=100
# a.company="amazon"        #instance
a.getsalary("atharv")       #another argument from self  sign
a.greet()


