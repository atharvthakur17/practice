class employe:
    comapany="bharat"
    salary=1000
    bonus=200
    @property                     # getter
    def totalsal(self):
        return self.salary+self.bonus
    @totalsal.setter              #setter
    def totalsal(self,val):
        self.bonus=val-self.salary

a=employe()
print(a.totalsal)
a.totalsal=10000
print(a.bonus)