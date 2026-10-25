class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print(self.name,"has got",self.marks,"marks")
    #return value
    def result(self):
        if self.marks>=50:
            return "pass"
        else:
            return "fail"
    #data change
    def add_bonus(self,bonus):
        self.marks=self.marks+bonus

s1=Student("Ali",50)
s2=Student("Ahmad",42)
s2.add_bonus(8)
print(s1.name, s1.result())
print(s2.name, s2.result())

class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
       self.balance=self.balance+amount
    def withdraw(self,amount):
        if self.balance>=amount:
         self.balance=self.balance-amount
        else:
            print("No enough balance")
    def show(self):
        print(self.owner,"have current balance",self.balance)
acc=Bank("Sara",1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)
acc.show()

    