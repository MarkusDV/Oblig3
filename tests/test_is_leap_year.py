# test_is_leap_year.py
import pytest
from is_leap_year import isLeapYear

def test_leap_year_divisible_by_4_but_not_100():
    assert isLeapYear(2004) == True

def test_leap_year_divisible_by_400():
    assert isLeapYear(2000) == True

def test_non_leap_year_not_divisible_by_4():
    assert isLeapYear(2005) == False

def test_non_leap_year_divisible_by_100_but_not_400():
    assert isLeapYear(1900) == False



