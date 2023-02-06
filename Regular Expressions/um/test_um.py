import pytest
from um import count


def test_singular():
    assert count("um") == 1
    assert count(" um   ") == 1
    assert count("UM") == 1


def test_multiple():
    assert count("um um um") == 3
    assert count("Um UM uM") == 3


def test_words():
    assert count("yum") == 0
    assert count("umami") == 0
    assert count("circumference") == 0


def test_sentence():
    assert count("Um, so anyways, um...") == 2
    assert count("Therefore, um, the circumstances, um, determine this!") == 2