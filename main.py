import pytest


def always_returns_true():
    alyssa = "cool"
    return True


def test_always_returns_true():
    assert always_returns_true()
