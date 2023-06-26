from bank import value

def test_value():
    assert value("hello") == 0

def test_withh1():
    assert value("hi") == 20

def test_withh():
    assert value("hey") == 20

def test_caps():
    assert value("Hey") == 20
