def orbital_period(a):
    """
    Calculate the orbital period T in years based on the semi-major axis a in AU
    using Kepler's Third Law: T^2 = a^3, therefore T = sqrt(a^3)
    """
    return (a**3)**0.5
