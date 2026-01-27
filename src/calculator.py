def _validate_inputs(x, y):
    """
    Validates that both inputs are numbers (int or float).
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")


def fun1(x, y):
    """
    Adds two numbers.
    """
    _validate_inputs(x, y)
    return x + y


def fun2(x, y):
    """
    Subtracts y from x.
    """
    _validate_inputs(x, y)
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers.
    """
    _validate_inputs(x, y)
    return x * y


def fun4(x, y):
    """
    Combines the results of fun1, fun2, and fun3 and returns their sum.
    """
    _validate_inputs(x, y)
    return fun1(x, y) + fun2(x, y) + fun3(x, y)
