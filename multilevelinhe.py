class person:
    def __init__(self):
        print("initializing person")
    def breath(self):
        print("im breathing ...")

class employe(person):
    company="google"
    def __init__(self):
        super().__init__()
        print("initializing empl")
        
    def breath(self):
        super().breath()
        print("im an employe , im brething")

class programmer(employe):
    def __init__(self):
        super().__init__()
        print("initializing prog")
        
    def salary(self):
        print("i have no salary")
    def breath(self):
        super().breath()
        print("im a programmer im braething ++")
p=person()
e=employe()       
pr=programmer()
# pr.breath()