Student={"name":"Ali","age":20,"city":"Lahore"}
print(Student)
print(Student["name"])
print(Student["city"])

#Lists and dictionaries
Students=[{"name":"Ali","age":20},{"name":"Sara","age":19},{"name":"Usman","age":22}]
for Student in Students:
    print(Student["name"],"ki age",Student["age"])