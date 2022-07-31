#we import the module we want to test.
import math_func

#we MUST create test methods with prefixes "test_", the after that can be any. For our case we used add and product
def test_add():
    #we then use assert key word to make assertions of expected answers.
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7  

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


#We then run as
#cd C:\Users\emwadun\OneDrive - Ericsson\Desktop\Projects\pytest-101
#py.test test_math_func.py

#pytest will give number of tests that passed.
#Pytest will Incase we assert wrong values in assertion or wrong maths sign in the module, Pytest will show the exact assertions that failed i.e. AssertionError.

#We can also use -v for verbose mode:
#py.test test_math_func.py -v

#- You can also run pytest using "py.test" only as your commend since we used a keyword test in prefix hence it will run pytest of your code.
#py.test or py.test -v
