from add import calculate_add

def test_positive_no():
    assert calculate_add(20,40) 

def test_zero():
    assert calculate_add(50,0) 

def test_negative():
    assert calculate_add(-50,10)