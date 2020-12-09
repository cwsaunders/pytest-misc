import math_func
import pytest

@pytest.mark.boolean # marker
def test_boolean(): # test_ prefix required for tests
    assert math_func.boolean(5,5) == True
    assert math_func.boolean(5,4) == False

@pytest.mark.number # marker
def test_addition():
    assert math_func.addition(4,1) == 5
    assert math_func.addition(6,6) == 12
    assert math_func.addition(6,6) == 13

@pytest.mark.skip(reason="Test Skip Option") # marker used to skip this test
def test_addition_two():
    assert math_func.addition(4,1) == 5
    assert math_func.addition(6,6) == 12
    assert math_func.addition(6,6) == 13