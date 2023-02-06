import pytest
from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")

def test_range():
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("127.393.322.199")
    assert not validate("1.2.344.4")

def test_format():
    assert not validate("cat")
    assert not validate("0123")
