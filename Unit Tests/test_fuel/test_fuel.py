import pytest
from fuel import convert, gauge


def test_fraction():
    assert convert("3/4") == 75
    assert convert("49/100") == 49
    assert convert("1/2") == 50


def test_fraction_error():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("3.14/5")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
