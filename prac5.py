class employe:
    comapany="bharat"
    salary=1000
    increment=2
    @property                     # getter
    def totalsal(self):
        return self.salary*self.increment
    @totalsal.setter              #setter
    def totalsal(self,val):
        self.increment=val/self.salary

a=employe()
print(a.totalsal)
a.totalsal=10000
print(a.increment)