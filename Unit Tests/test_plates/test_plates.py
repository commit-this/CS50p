from plates import is_valid


def test_length():
    assert not is_valid("awpofjapwjfpasfasd55550")
    assert not is_valid("C")


def test_alphanumeric():
    assert not is_valid("CS,%0")
    assert not is_valid("CS50!")


def test_first_two():
    assert not is_valid("C550")


def test_numbers():
    assert not is_valid("CS05")
    assert not is_valid("CS50P")


def test_valid():
    assert is_valid("CS50")
