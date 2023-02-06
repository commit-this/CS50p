import pytest
from seasons import seasonize
from datetime import date, timedelta


def test_invalid():
    with pytest.raises(SystemExit):
        seasonize("10-01-2020")
    with pytest.raises(SystemExit):
        seasonize("January 1, 2000")
    with pytest.raises(SystemExit):
        seasonize("3/3/1950")
    with pytest.raises(SystemExit):
        seasonize("2001-13-24")


def test_previous_year():
    assert (
        seasonize(str(date.today() - timedelta(days=365)))
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_two_years_ago():
    assert (
        seasonize(str(date.today() - timedelta(days=365 * 2)))
        == "One million, fifty-one thousand, two hundred minutes"
    )
