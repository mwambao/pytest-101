#we import the module we want to test
import math_func
import pytest #Lets import pytest since we need to use decorators for marks.
import sys
#we MUST create test methods with prefixes "test_", the after that can be any. For our case we used add and product
#If we dont use this prefix, the module without the prefix test_ wont be tested.

#lets skip this one
@pytest.mark.skip(reason="Do not run number add test")
def test_add():
    #we then use assert key word to make assertions of expected answers.
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 2
    assert math_func.add(5) == 7  

#Lets skip this one with condition, we will use skipiff decorator

@pytest.mark.skipif(sys.version_info == (3, 8), reason="Do not run product test")
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14
    print(math_func.product(5, 9))

@pytest.mark.strings #decorator
def test_add_strings():
    result = math_func.add("Hello", " World")

    assert result == "Hello World"
    assert type(result) is str
    assert "Hello" in result


#We then run as
#cd C:\Users\emwadun\OneDrive - Ericsson\Desktop\Projects\pytest-101
#py.test test_math_func.py

#pytest will give number of tests that passed.
#Pytest will Incase we assert wrong values in assertion or wrong maths sign in the module, Pytest will show the exact assertions that failed i.e. AssertionError.

#We can also use -v for verbose mode:
#py.test test_math_func.py -v

#- You can also run pytest using "py.test" only as your commend since we used a keyword test in prefix hence it will run pytest of your code.
#py.test or py.test -v

#-If you want to want to run specific test you can run as follows:
#py.test test_math_func.py::test_add -v

#If we want to run unit tests that have specific key words, we can use -k flag e.g. to run unit tests with 'add' key word:
#py.test test_math_func.py -v -k "add"
#test_math_func.py::test_add PASSED                                                                                               [ 50%] 
#test_math_func.py::test_add_strings PASSED                                                                                       [100%] 


#To skip a test we use skip decorator like given below and we give a reason:
#@pytest.mark.skip(reason="Do not run number add test")