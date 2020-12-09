import math_func

def test_boolean():
    assert math_func.boolean(5,5) == True
    assert math_func.boolean(5,4) == True

def test_addition():
    assert math_func.addition(4,1) == 5
    assert math_func.addition(6,6) == 11

