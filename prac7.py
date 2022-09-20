class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self): 
        str=""
        index=0
        for i in self.vec:
            str+=f" {i}a{index} +"
            index+=1
        return str[1:-1]
    def __add__(self,vec2):
        str2=[]
        if len(self.vec)==len(vec2.vec):
            for i in range (len(self.vec)):
                str2.append(self.vec[i]+vec2.vec[i])
            return vector(str2)
        else :
            return("not equal") 
    def __mul__(self,vec2):
        s=0
        if len(self.vec)==len(vec2.vec):
            for i in range (len(self.vec)):
                s+=(self.vec[i]*vec2.vec[i])
            return s 
        else:
            return("not equal")
        

v=vector([1,3,4])
v2=vector([2,3,5,6])
print(v+v2)
print(v*v2)