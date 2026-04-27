import numpy as np
import matplotlib.pyplot as plt

from mzi_noise import mzi_output_lossy, add_noise


P1 = 1.0
P2 = 1.0
alpha1 = 1.0
alpha2 = 0.7

sigma = 0.2  # noise level

# logic states
phi_0 = np.pi      # should be logic 0
phi_1 = 0          # should be logic 1

N = 10000

errors = 0

I0_values = []
I1_values = []

for _ in range(N):
    I0 = mzi_output_lossy(P1, P2, phi_0, alpha1, alpha2)
    I1 = mzi_output_lossy(P1, P2, phi_1, alpha1, alpha2)

    I0_noisy = add_noise(I0, sigma)
    I1_noisy = add_noise(I1, sigma)

    I0_values.append(I0_noisy)
    I1_values.append(I1_noisy)

# umbral
T = (np.mean(I0_values) + np.mean(I1_values)) / 2

# calcular errores
for i in range(N):
    if I0_values[i] > T:  # debería ser 0
        errors += 1
    if I1_values[i] < T:  # debería ser 1
        errors += 1

error_rate = errors / (2 * N)

print("Threshold:", T)
print("Error rate:", error_rate)

# visualizar
plt.hist(I0_values, bins=50, alpha=0.5, label="Logical 0")
plt.hist(I1_values, bins=50, alpha=0.5, label="Logical 1")

plt.axvline(T, color='red', linestyle='--', label="Threshold")

plt.legend()
plt.title("Noise and decision regions")
plt.show() 
