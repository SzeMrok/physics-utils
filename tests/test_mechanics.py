from physics_utils.mechanics import kinetic_energy
from physics_utils import _si


def test_kinetic_energy():
    mass = 10  # kg
    velocity = 5  # m/s
    expected_ke = 125.0 * _si.J # J
    
    calculated_ke = kinetic_energy(mass, velocity)
    
    assert abs((calculated_ke - expected_ke).magnitude) < 1e-6, \
        f"Expected {expected_ke} J, got {calculated_ke} J"
