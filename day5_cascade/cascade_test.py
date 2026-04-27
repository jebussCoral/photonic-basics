import os
import sys
import numpy as np

# Allow importing code from day4_xor when running this file from day5_cascade
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from day4_xor.xor_mzi_realistic import xor_mzi_noisy, decide


# System parameters
alpha2 = 0.7
sigma = 0.1
N = 1000


def xor_cascade(A, B, E, threshold=0.5):
    """
    Two-stage XOR cascade:

    C = A XOR B
    D = C XOR E

    The first XOR output is noisy and continuous.
    We convert it back to a logical value using a threshold.
    """

    # First XOR gate
    C_value = xor_mzi_noisy(A, B, alpha2=alpha2, sigma=sigma)

    # Regenerate intermediate logic level
    C_logic = decide(C_value, threshold)

    # Second XOR gate
    D_value = xor_mzi_noisy(C_logic, E, alpha2=alpha2, sigma=sigma)

    return D_value


def ideal_cascade(A, B, E):
    """
    Ideal digital reference:

    D = (A XOR B) XOR E
    """
    return (A ^ B) ^ E


test_cases = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
]


errors = 0
total = 0

for _ in range(N):
    for A, B, E in test_cases:
        output_value = xor_cascade(A, B, E, threshold=0.5)
        predicted = decide(output_value, 0.5)

        expected = ideal_cascade(A, B, E)

        if predicted != expected:
            errors += 1

        total += 1


error_rate = errors / total

print("Cascade simulation")
print("------------------")
print("alpha2:", alpha2)
print("sigma:", sigma)
print("N:", N)
print("Total decisions:", total)
print("Errors:", errors)
print("Cascade error rate:", error_rate)