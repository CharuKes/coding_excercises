from plates import is_valid

def main():
    print(test_is_valid())


def test_is_valid():
    assert is_valid("123456") == False

def test_one():
    assert is_valid("ASD33012") == False

def test_two():
    assert is_valid("ASDO3P") == False


def test_three():
    assert is_valid("AB0000") == False

def test_four():
    assert is_valid("AB:?..") == False


if __name__ == "__main__":
    main()