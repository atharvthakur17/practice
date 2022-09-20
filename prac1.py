class programmer:
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def info(self):
        print(f"name is {self.name} prduct is {self.product} in company {self.company}")
a=programmer("atharv","github")
a.info()
b=programmer("aaaa","haid")
b.info()