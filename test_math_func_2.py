from math_func import StudentDB
import pytest

@pytest.fixture(scope='module') # Scope only calls DB setup once, not at beginning of every test run
def db():
    print('------------Setup------------')
    db = StudentDB()
    db.connect('data.json')
    yield db # yield instead of return so that the close() is executed at the end of the tests
    print('------------Teardown------------')
    db.close()

def test_scott_data(db): # returned db argument from @pytest.fixture
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db): # returned db argument from @pytest.fixture
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'