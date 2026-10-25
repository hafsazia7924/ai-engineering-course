fruits=["apple","banana","mango"]
fruits.append("orange")
print(fruits)
fruits[1]="grapes"
print(fruits)
fruits.remove("mango")
print(fruits)
print(len(fruits))    #length
for fruit in fruits:
    print ("i like ",fruit)