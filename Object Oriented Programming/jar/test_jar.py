import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    newjar = Jar(25)
    assert newjar.capacity == 25
    with pytest.raises(ValueError):
        Jar(2.4)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(1)
    assert jar.size == 4


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
