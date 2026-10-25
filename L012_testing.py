def add(a, b):
    return a + b

assert add(2, 3) == 5
print("Test 1 passed")

#test function
def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"

test_add()
print("All tests passed")

#practical
def is_adult(age):
    return age>=18
def test_is_adult():
     assert is_adult(18)==True, "is an adult"
     assert is_adult(17)==False, "age should be 18" 
     assert is_adult(19)==True, "an adult"
test_is_adult()
print("is_adult tests passed")