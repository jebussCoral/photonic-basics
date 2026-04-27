import numpy as np


def mzi_output_lossy(P1, P2, phi, alpha1=1.0, alpha2=1.0):
    E1 = np.sqrt(P1) * alpha1
    E2 = np.sqrt(P2) * alpha2

    E_out = E1 + E2 * np.exp(1j * phi)
    I_out = np.abs(E_out) ** 2

    return I_out


def add_noise(intensity, sigma):
    noise = np.random.normal(0, sigma)
    return intensity + noise 
