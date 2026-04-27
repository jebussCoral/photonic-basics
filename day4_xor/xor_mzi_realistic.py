import numpy as np


def phase_encode(bit):
    return bit * np.pi


def mzi_lossy(phi_diff, alpha1=1.0, alpha2=1.0):
    E1 = 1 * alpha1
    E2 = np.exp(1j * phi_diff) * alpha2

    E_out = E1 + E2
    I_out = np.abs(E_out) ** 2

    return I_out


def xnor_mzi_realistic(A, B, alpha1=1.0, alpha2=1.0):
    phi1 = phase_encode(A)
    phi2 = phase_encode(B)
    phi_diff = phi1 - phi2

    return mzi_lossy(phi_diff, alpha1, alpha2)


def xor_mzi_realistic(A, B, alpha1=1.0, alpha2=1.0):
    xnor = xnor_mzi_realistic(A, B, alpha1, alpha2)
    xnor_norm = xnor / 4
    xor = 1 - xnor_norm

    return xor


def add_noise(value, sigma):
    noise = np.random.normal(0, sigma)
    return value + noise


def xor_mzi_noisy(A, B, alpha1=1.0, alpha2=1.0, sigma=0.0):
    clean = xor_mzi_realistic(A, B, alpha1, alpha2)
    noisy = add_noise(clean, sigma)

    return noisy


def decide(value, threshold):
    return 1 if value > threshold else 0