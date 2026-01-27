# Is Even: Complete
A Python Module that answers the question that few programmers and mathematicians dares to even approach: Is it even? 

## Content

### `real_is_even(number: float) -> bool`
Determines if a real number is even. Supports integers, floats, and mathematical constants.

**Features:**
- Works with integers, and floats
- Handles mathematical constants like π and e
- Validates that your input is actually real (no imaginary numbers here!)

### `complex_is_even(number: complex) -> bool`
Determines if a complex number is even. A complex number is considered even if both its real and imaginary parts have the same parity.

**Features:**
- Treats complex numbers with sophisticated mathematical grace
- Knows the answer to "is `i` even?"
- Validates that you actually input a complex number

### `general_is_even(number: int|float|complex) -> bool`
Determines if a number, either real or complex, is even.

**Features:**
- Supports all currently known numbers, both real and unreal!

## Usage

```python
from even_or_odd import real_is_even, complex_is_even, general_is_even

# Real numbers
real_is_even(2)           # True
real_is_even(3.7)         # False
real_is_even(2.4)         # True

# Complex numbers
complex_is_even(2+2j)     # True (both parts even)
complex_is_even(3+3j)     # True (both parts odd)
complex_is_even(2+3j)     # False (mixed parity)

# General numbers
general_is_even(2+2j)     # True
general_is_even(3.7)      # False
```

## Testing

Run the professional test suite with:
```bash
python tests.py
```
