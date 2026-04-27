import numpy as np


def optical_field(power):
    return np.sqrt(power)


def mzi_output(P1, P2, phi):
    E1 = optical_field(P1)
    E2 = optical_field(P2)

    E_out = E1 + E2 * np.exp(1j * phi)
    I_out = np.abs(E_out) ** 2

    return I_out