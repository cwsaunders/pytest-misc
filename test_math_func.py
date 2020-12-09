import math_func

def test_boolean(): # test_ prefix required for tests
    assert math_func.boolean(5,5) == True
    assert math_func.boolean(5,4) == False

def test_addition():
    assert math_func.addition(4,1) == 5
    assert math_func.addition(6,6) == 12
    assert math_func.addition(6,6) == 13

