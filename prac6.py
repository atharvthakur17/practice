class complex:
    def __init__(self,real,img):
        self.r=real
        self.i=img
    
    def __add__(self,c):
        return complex(self.r+c.r,self.i+c.i)

    def __str__(self):
        return f"{self.r},{self.i}"

c1=complex(1,4)
c2=complex(2,5)        
print(c1+c2)