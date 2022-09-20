class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("lets print")
        return(self.num+num2.num)
n1=number(4)
n2=number(5)
print(n1+n2)