print("**Number Analysis Program**")
integer=input("Enter a positive integer")
integer=int(integer)
print("Your entered integer is",integer)
n=[]
x=0
for i in range(integer):
    i+=1
    n.append(i)
    x=x+i
print(n)
print ("The sum for all is",x)   
    