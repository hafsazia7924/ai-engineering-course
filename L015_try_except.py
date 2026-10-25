def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide(10, 2)
divide(10, 0)
print("Program finished")

#Catching different errors
def divide_text(a_text, b_text):
    try:
        a = int(a_text)
        b = int(b_text)
        print("Result:", a / b)
    except ValueError:
        print("Please enter whole numbers only")
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide_text("10", "2")
divide_text("ten", "2")
divide_text("10", "0")

#except ValueError as e
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)

print(check_age(20))

#One final example using several of them
def average(numbers: list[float]) -> float:
    if len(numbers) == 0:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

try:
    print(average([10, 20, 30]))
    print(average([]))
except ValueError as e:
    print("Error:", e)