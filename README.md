# novel-conjecture-and-computational-evidence.
A research project exploring the relationship between Fermat primes and Mersenne primes, a novel conjecture and computational evidence.
# Lucas-Lehmer Primality Test Using FFT

## Overview

This repository contains a Python implementation of the Lucas-Lehmer primality test, optimized using the Fast Fourier Transform (FFT). The test is designed to verify whether a given Mersenne number \( M_p = 2^p - 1 \) is prime, where \( p \) is a prime number.

## Background

Mersenne primes are of the form \( M_p = 2^p - 1 \), where \( p \) itself is a prime number. The Lucas-Lehmer test is an efficient algorithm used specifically to determine the primality of such numbers. By leveraging FFT, this implementation allows for fast multiplication of large integers, making it suitable for testing extremely large values of \( p \).

## Script Explanation

### `fft_multiply(a, b)`

- Multiplies two large integers using their coefficient representation and FFT.
- Returns the coefficients of the resulting product.

### `modular_reduce(x, mod)`

- Reduces the polynomial coefficients modulo \( 2^p - 1 \), ensuring the result fits within the required bounds.

### `lucas_lehmer_fft(p)`

- Performs the Lucas-Lehmer test for the Mersenne number \( M_p = 2^p - 1 \).
- Returns `True` if \( M_p \) is prime, otherwise returns `False`.

## Usage

1. Replace the placeholder `'Inclure p'` with the prime number \( p \) you wish to test.
2. Run the script. If the output is "YES", then \( 2^p - 1 \) is a Mersenne prime. If "NO", it is not.

## Example

To test whether \( M_{31} = 2^{31} - 1 \) is a Mersenne prime:

```python
p = 31
if lucas_lehmer_fft(p):
    print("YES")
else:
    print("NO")
