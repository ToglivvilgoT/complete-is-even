import re


def real_is_even(rational_number: float) -> bool:
    """
    Determine if a rational number is even.

    Args:
        rational_number (float): The rational number to check.

    Returns:
        bool: True if the number is even, False otherwise.

    Raises:
        ValueError: If the number is not rational.
    """
    if type(rational_number) not in [float, int]:
        raise ValueError("The number is not rational.")
    digs = str(rational_number).split(".")
    if len(digs) != 2:
        return int(digs[0][-1]) % 2 == 0
    if not bool(re.search(r"\.0*[1-9]", digs[1])):
        return int(digs[0][-1]) % 2 == 0
    dig = int(digs[-1])
    return (
        dig % 2 == 0
        if (dig in [1, 2, 3, 4, 5, 6, 7, 8, 9])
        else real_is_even(float(str(rational_number)[:-1]))
    )


def complex_is_even(complex_number: complex) -> bool:
    """
    Determine if a complex number is even based on its real and imaginary parts.

    Args:
        complex_number (complex): The complex number to check.

    Returns:
        bool: True if the complex number is considered even, False otherwise.

    Raises:
        ValueError: If either the real or imaginary part is not real, or the number is not a complex number.
    """
    if type(complex_number) is not complex:
        raise ValueError("The number is not a complex number.")
    return (
        real_is_even(complex_number.real) and real_is_even(complex_number.imag)
    ) or (
        not real_is_even(complex_number.real) and not real_is_even(complex_number.imag)
    )


def general_is_even(number: int | float | complex) -> bool:
    """
    Determine if a number (real or complex) is even.

    Args:
        number (int|float|complex): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.

    Raises:
        ValueError: If the number is neither real nor complex.
    """
    if type(number) in [int, float]:
        return real_is_even(number)
    elif type(number) is complex:
        return complex_is_even(number)
    else:
        raise ValueError("Number is not a number.")
