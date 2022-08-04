import math_func
import pytest

@pytest.mark.parametrize('num1, num2, result', 
                        [
                         (7,3,10), 
                         ('Rat', 'Race', 'RatRace'),
                         (10.5, 25.5, 36)
                        ]
                        )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result

#Execution output
#test_math_func4.py::test_add[7-3-10] PASSED             [33%] 
#test_math_func4.py::test_add[Rat-Race-RatRace] PASSED   [66%]
#test_math_func4.py::test_add[10.5-25.5-36] PASSED      [100%] 