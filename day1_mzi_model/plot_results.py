import numpy as np
import matplotlib .pyplot as plt
from mzi import mzi_output

P1 = 1.0
P2 = 0.5

phi_values = np.linspace(0,2 * np.pi, 500)
intensity_values = [mzi_output(P1,P2,phi) for phi in phi_values]

plt.plot(phi_values,intensity_values)
plt.show()