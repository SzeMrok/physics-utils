from physics_utils.mechanics import kinetic_energy


def test_kinetic_energy():
    mass = 10  # kg
    velocity = 5  # m/s
    expected_ke = 125  # J
    
    calculated_ke = kinetic_energy(mass, velocity)
    
    assert abs(calculated_ke - expected_ke) < 1e-6, \
        f"Expected {expected_ke} J, got {calculated_ke} J"
