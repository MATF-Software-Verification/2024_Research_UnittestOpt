def abs_divide(a, b):
    """
    Divides two numbers together and return absoulute value of the result.

    Args:
        a: First number
        b: Second number

    Returns:
        Absolut value of the division result or None if b is zero.
    """
    if b == 0:
        return None
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return a / b
    else:
        return -(a / b)