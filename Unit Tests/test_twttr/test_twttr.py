from twttr import shorten


def test_capitalization():
    assert shorten("Twitter") == "Twttr"
    assert shorten("tWtTER") == "tWtTR"


def test_sentence():
    assert shorten("Hello, how are you?") == "Hll, hw r y?"


def test_no_vowels():
    assert shorten("CS50") == "CS50"
