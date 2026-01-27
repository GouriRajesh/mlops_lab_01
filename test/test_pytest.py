import pytest
from src.calculator import fun1,fun2,fun3,fun4


# -------------------
# Tests for fun1 (addition)
# -------------------

def test_fun1_valid_inputs():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0
    assert fun1(2.5, 1.5) == 4.0


def test_fun1_invalid_inputs():
    with pytest.raises(ValueError):
        fun1("2", 3)


# -------------------
# Tests for fun2 (subtraction)
# -------------------

def test_fun2_valid_inputs():
    assert fun2(5, 3) == 2
    assert fun2(0, 5) == -5
    assert fun2(2.5, 1.5) == 1.0


def test_fun2_invalid_inputs():
    with pytest.raises(ValueError):
        fun2(5, None)


# -------------------
# Tests for fun3 (multiplication)
# -------------------

def test_fun3_valid_inputs():
    assert fun3(2, 3) == 6
    assert fun3(-2, 3) == -6
    assert fun3(2.5, 2) == 5.0


def test_fun3_invalid_inputs():
    with pytest.raises(ValueError):
        fun3([], 3)


# -------------------
# Tests for fun4 (combined function)
# fun4(x, y) = fun1 + fun2 + fun3
# -------------------

def test_fun4_valid_inputs():
    # fun1(3,2)=5, fun2(3,2)=1, fun3(3,2)=6 → total = 12
    assert fun4(3, 2) == 12

    # fun1(2,2)=4, fun2(2,2)=0, fun3(2,2)=4 → total = 8
    assert fun4(2, 2) == 8


def test_fun4_invalid_inputs():
    with pytest.raises(ValueError):
        fun4("a", "b")
