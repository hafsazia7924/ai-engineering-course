class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def say_hello(self):
    print("hello my name is", self.name)
  def birthday(self):
    self.age=self.age+1
    print(self.name , "is now " , self.age , "years old")
s1=Student("Ali",20)
s2=Student("Sara",19)
s1.say_hello()
s2.say_hello()
s1.birthday()
s2.birthday()
print(s2.age)
 