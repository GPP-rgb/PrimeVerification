import numpy as np
from numpy.fft import fft, ifft

def fft_multiply(a, b):
    # Multiplies two large integers using FFT
    A = fft(a)
    B = fft(b)
    C = A * B
    c = ifft(C).real.round().astype(int)
    return c

def modular_reduce(x, mod):
    # Reduce polynomial coefficients by modulo
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    for i in range(len(x) - 1, mod, -1):
        if x[i] != 0:
            for j in range(mod):
                x[i - mod + j] += x[i]
            x[i] = 0
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x

def lucas_lehmer_fft(p):
    # Lucas-Lehmer test using FFT
    M_p = (1 << p) - 1  # 2^p - 1
    s = [4]
    for _ in range(p - 2):
        s = fft_multiply(s, s)  # s^2 using FFT
        s[0] -= 2  # Subtract 2
        s = modular_reduce(s, p)  # Reduce modulo 2^p - 1
        s = [x % 2 for x in s]  # Coefficients modulo 2
    return s == [0]

p = 'p value'
if lucas_lehmer_fft(p):
    print("YES")
else:
    print("NO")
