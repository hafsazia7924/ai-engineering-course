class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name,"speaks")
class Dog(Animal):
    def bark(self):
        print(self.name,"says woof")
class Cat(Animal):
    def meow(self):
        print(self.name,"says meowww")
class Cow(Animal):
    def speak(self):
        print(self.name,"says:Moo!")
a=[Dog("Tom"),Cat("bella"),Cow("Gulabo"),Animal("loin")]
for a in a:
    a.speak()

#super() and __str__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name},Age{self.age}"
class student(person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def __str__(self):
        return f"{self.name},Age{self.age},Roll No.{self.rollno}"
s1=student("Ali",20,13)
print(s1.name)
print(s1.age)
print(s1.rollno)
print(s1)