def add(a: int,b:int)->int:    #type hint
    return a+b
print(add(10,20))
def greet(name: str, marks: float)->str:
    return "hello "+name+", your marks are "+str(marks)
print(greet("Ali",49.5))

#List
def average(marks: list[int], bonus: int = 5) -> float:
    total = sum(marks) + bonus
    return total / len(marks)


print(average([60, 70, 80]))
print(average([60, 70, 80], 0))

