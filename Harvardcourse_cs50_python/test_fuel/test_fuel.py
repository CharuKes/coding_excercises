from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25

def test_match():
    with pytest.raises(ValueError):
        convert("5/2")
def test_match1():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"