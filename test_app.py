from app import get_employees

def test_employee_count():
    assert len(get_employees()) == 3

def test_first_employee():
    assert get_employees()[0] == "John"
