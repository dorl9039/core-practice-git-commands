import pytest


def always_returns_true():
    variable = "Alyssa"
    return True



def test_always_returns_true():
    assert always_returns_true()
