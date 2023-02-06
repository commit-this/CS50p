from bank import value


def test_default():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("f") == 100
    assert value("") == 100


def test_capitalization():
    assert value("HeLLo") == 0
    assert value("Hey") == 20


def test_sentence():
    assert value("why hello there, sir!") == 100


# def test_misc():
#     assert value("     hello  ") == 0
#     assert value("hhHHHhHHhHhHhHello") == 20
#     assert value("29239") == 100
