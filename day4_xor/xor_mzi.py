import numpy as np

def phase_encode(bit):
    """
    Encode logical bit into phase.
    0 → 0
    1 → pi
    """
    return bit * np.pi

def mzi_phase_output(phi_diff):
    """
    MZI response as function of phase difference.
    """
    E1 = 1
    E2 = np.exp(1j * phi_diff)

    E_out = E1 + E2
    I_out = np.abs(E_out) ** 2

    return I_out

def xnor_mzi(A, B):
    phi1 = phase_encode(A)
    phi2 = phase_encode(B)

    phi_diff = phi1 - phi2

    intensity = mzi_phase_output(phi_diff)

    return intensity

def xor_mzi(A, B):
    xnor_intensity = xnor_mzi(A, B)

    xnor_normalized = xnor_intensity / 4

    xor_output = 1 - xnor_normalized

    return xor_output