numbers=[1,2,3,4,5]
square=[]
for i in numbers:
    square.append(i*i)
print(square)

#same thing
squares=[i*i for i in numbers]
print(squares)

#adding filter
marks=[123,176,188,169,133]
passed=[i for i in marks if i>150]
print(passed)

#clearing names
names=["  Ali  ","sara","usMan"]
clean=[name.strip().lower() for name in names]
print(clean)

prices=[50,1200,90,560,1500]
tax=[n*1.1 for n in prices]
print(tax)