from re import L


class railwayform():
    def printdata(self):
        print(f"the name of train is {self.train}")
        print(f"name of traveller {self.name}")

a=railwayform()
a.train=input("train ")
a.name=input("name ")
a.printdata()