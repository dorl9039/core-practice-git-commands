import pytest


def always_returns_true():
    variable = "Alyssa"
    doris = "very cool"
    return True



def test_always_returns_true():
    assert always_returns_true()
