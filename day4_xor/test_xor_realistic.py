import numpy as np

from xor_mzi_realistic import xor_mzi_noisy, decide


alpha2 = 0.6
sigma = 0.2
N = 1000

samples_0 = []
samples_1 = []

for _ in range(N):
    # Cases that should output logical 0
    samples_0.append(xor_mzi_noisy(0, 0, alpha2=alpha2, sigma=sigma))
    samples_0.append(xor_mzi_noisy(1, 1, alpha2=alpha2, sigma=sigma))

    # Cases that should output logical 1
    samples_1.append(xor_mzi_noisy(0, 1, alpha2=alpha2, sigma=sigma))
    samples_1.append(xor_mzi_noisy(1, 0, alpha2=alpha2, sigma=sigma))

mu0 = np.mean(samples_0)
mu1 = np.mean(samples_1)
delta = mu1 - mu0

T = (mu0 + mu1) / 2

print("mu0 (logical 0):", mu0)
print("mu1 (logical 1):", mu1)
print("Delta (separation):", delta)
print("Sigma (noise):", sigma)
print("Delta / Sigma:", delta / sigma)
print("Threshold:", T)

errors = 0
total = 0

test_cases = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
]

for _ in range(N):
    for A, B, expected in test_cases:
        value = xor_mzi_noisy(A, B, alpha2=alpha2, sigma=sigma)
        predicted = decide(value, T)

        if predicted != expected:
            errors += 1

        total += 1

error_rate = errors / total

print("Error rate:", error_rate)