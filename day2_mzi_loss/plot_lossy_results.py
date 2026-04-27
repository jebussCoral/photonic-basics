import numpy as np
import matplotlib.pyplot as plt

from mzi_lossy import mzi_output_lossy


P1 = 1.0
P2 = 1.0

phi_values = np.linspace(0, 2 * np.pi, 500)

ideal_values = [
    mzi_output_lossy(P1, P2, phi, alpha1=1.0, alpha2=1.0)
    for phi in phi_values
]

lossy_values = [
    mzi_output_lossy(P1, P2, phi, alpha1=1.0, alpha2=0.3)
    for phi in phi_values
]

print("Ideal minimum:", min(ideal_values))
print("Ideal maximum:", max(ideal_values))
print("Lossy minimum:", min(lossy_values))
print("Lossy maximum:", max(lossy_values))

plt.figure()
plt.plot(phi_values, ideal_values, label="Ideal MZI")
plt.plot(phi_values, lossy_values, label="Lossy MZI: alpha2 = 0.3")

plt.title("Ideal vs Lossy MZI")
plt.xlabel("Phase difference phi (rad)")
plt.ylabel("Output intensity")
plt.grid(True)
plt.legend()

plt.savefig("day2_lossy_mzi_result.png", dpi=300)
plt.show()