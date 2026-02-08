"""Unit tests for even_or_odd module."""

import math
import unittest

from init import int_is_even, complex_is_even, real_is_even, general_is_even


class TestIntIsEven(unittest.TestCase):
    """Tests for the int_is_even() function."""

    def test_even_integers(self) -> None:
        """Test that even integers are correctly identified."""
        self.assertTrue(int_is_even(2))
        self.assertTrue(int_is_even(0))

    def test_odd_integers(self) -> None:
        """Test that odd integers are correctly identified."""
        self.assertFalse(int_is_even(3))

    def test_invalid_input_raises_error(self) -> None:
        """Test that non-integer types raise TypeError."""
        with self.assertRaises(TypeError):
            int_is_even("not a number")


class TestRealIsEven(unittest.TestCase):
    """Tests for the real_is_even function."""

    def test_even_integers(self) -> None:
        """Test that even integers are correctly identified."""
        self.assertTrue(real_is_even(2))
        self.assertTrue(real_is_even(0))

    def test_odd_integers(self) -> None:
        """Test that odd integers are correctly identified."""
        self.assertFalse(real_is_even(3))

    def test_even_floats(self) -> None:
        """Test that even floats are correctly identified."""
        self.assertTrue(real_is_even(2.0))
        self.assertTrue(real_is_even(2.000))

    def test_odd_floats(self) -> None:
        """Test that odd floats are correctly identified."""
        self.assertFalse(real_is_even(3.0))
        self.assertFalse(real_is_even(3.000))

    def test_decimal_numbers(self) -> None:
        """Test decimal numbers with fractional parts."""
        self.assertTrue(real_is_even(2.4))
        self.assertFalse(real_is_even(3.7))

    def test_mathematical_constants(self) -> None:
        """Test behavior with mathematical constants."""
        self.assertFalse(real_is_even(math.pi))
        self.assertTrue(real_is_even(math.e))

    def test_zero(self) -> None:
        """Test that zero is even."""
        self.assertTrue(real_is_even(0.0))

    def test_invalid_input_raises_error(self) -> None:
        """Test that non-rational types raise ValueError."""
        with self.assertRaises(ValueError):
            real_is_even("not a number")


class TestComplexIsEven(unittest.TestCase):
    """Tests for the complex_is_even function."""

    def test_both_parts_even(self) -> None:
        """Test complex numbers with both even parts."""
        self.assertTrue(complex_is_even(complex(2, 2)))
        self.assertTrue(complex_is_even(complex(4, 4)))

    def test_both_parts_odd(self) -> None:
        """Test complex numbers with both odd parts."""
        self.assertTrue(complex_is_even(complex(3, 3)))
        self.assertTrue(complex_is_even(complex(5, 5)))

    def test_mixed_parity(self) -> None:
        """Test complex numbers with mixed even/odd parts."""
        self.assertFalse(complex_is_even(complex(2, 3)))
        self.assertFalse(complex_is_even(complex(3, 2)))

    def test_invalid_input_raises_error(self) -> None:
        """Test that non-complex types raise ValueError."""
        with self.assertRaises(ValueError):
            complex_is_even(42)


class TestGeneralIsEven(unittest.TestCase):
    """Tests for the general_is_even function."""

    def test_integer_even(self) -> None:
        """Test that even integers are correctly identified via general function."""
        self.assertTrue(general_is_even(2))
        self.assertTrue(general_is_even(0))
        self.assertTrue(general_is_even(42))

    def test_integer_odd(self) -> None:
        """Test that odd integers are correctly identified via general function."""
        self.assertFalse(general_is_even(3))
        self.assertFalse(general_is_even(1))
        self.assertFalse(general_is_even(99))

    def test_float_even(self) -> None:
        """Test that even floats are correctly identified via general function."""
        self.assertTrue(general_is_even(2.0))
        self.assertTrue(general_is_even(2.4))

    def test_float_odd(self) -> None:
        """Test that odd floats are correctly identified via general function."""
        self.assertFalse(general_is_even(3.0))
        self.assertFalse(general_is_even(3.7))

    def test_complex_both_even(self) -> None:
        """Test complex numbers with both even parts via general function."""
        self.assertTrue(general_is_even(complex(2, 2)))
        self.assertTrue(general_is_even(complex(4, 4)))

    def test_complex_both_odd(self) -> None:
        """Test complex numbers with both odd parts via general function."""
        self.assertTrue(general_is_even(complex(3, 3)))
        self.assertTrue(general_is_even(complex(5, 5)))

    def test_complex_mixed_parity(self) -> None:
        """Test complex numbers with mixed parity via general function."""
        self.assertFalse(general_is_even(complex(2, 3)))
        self.assertFalse(general_is_even(complex(3, 2)))

    def test_mathematical_constants(self) -> None:
        """Test behavior with mathematical constants via general function."""
        self.assertFalse(general_is_even(math.pi))
        self.assertTrue(general_is_even(math.e))

    def test_invalid_input_raises_error(self) -> None:
        """Test that invalid types raise ValueError."""
        with self.assertRaises(ValueError):
            general_is_even("not a number")
        with self.assertRaises(ValueError):
            general_is_even([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
