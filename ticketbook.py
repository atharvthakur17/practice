class train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    def info(self):
        print(f"train name is {self.name} and seats available {self.seats}")
        print(f"fare is {self.fare}")   
    def book(self):
        if self.seats>0:
            print("****your ticket has been booked*****")
            self.seats=self.seats-1
    def cancel(self):
        print("***ticket has been canceled***")
        self.seats+=1


a=train("rajdhani",100,35)
a.info()
a.book()
a.info()
a.cancel()
a.info()

