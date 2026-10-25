#zero division error correction
def average(marks):
    if len(marks)>0:
     total = sum(marks)
     return total / len(marks) 
    else:
       raise ValueError("marks cannot be empty")

def report(name, marks):
    avg = average(marks)
    print(name, "average:", avg)


report("Ali", [80, 90, 70])
report("Sara", [1])


