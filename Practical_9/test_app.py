from hypothesis import given
from hypothesis import strategies as st

from app import add, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(3, 4) == 12


@given(st.integers(), st.integers())
def test_add_hypothesis(a, b):
    assert add(a, b) == a + b
