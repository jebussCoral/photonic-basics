import numpy as np


def optical_field(power):
    """
    Convert optical power into optical field amplitude.

    Power is proportional to |E|^2, therefore:
    E = sqrt(P)
    """
    return np.sqrt(power)


def apply_loss(field, alpha):
    """
    Apply optical field loss.

    alpha = 1.0 means no loss.
    alpha < 1.0 means attenuation of the optical field.
    """
    return field * alpha


def mzi_output_lossy(P1, P2, phi, alpha1=1.0, alpha2=1.0):
    """
    Compute the output intensity of a lossy Mach-Zehnder Interferometer.

    Parameters
    ----------
    P1 : float
        Optical power in arm 1.
    P2 : float
        Optical power in arm 2.
    phi : float
        Phase difference between both arms, in radians.
    alpha1 : float
        Field transmission factor in arm 1.
    alpha2 : float
        Field transmission factor in arm 2.

    Returns
    -------
    float
        Output optical intensity.
    """
    E1 = optical_field(P1)
    E2 = optical_field(P2)

    E1_lossy = apply_loss(E1, alpha1)
    E2_lossy = apply_loss(E2, alpha2)

    E_out = E1_lossy + E2_lossy * np.exp(1j * phi)
    I_out = np.abs(E_out) ** 2

    return I_out 
