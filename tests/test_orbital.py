from physics_utils.orbital import escape_velocity


def test_escape_velocity():
    
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6  # m
    expected_escape_velocity = 11186  # m/s
    
    calculated_escape_velocity = escape_velocity(earth_mass, earth_radius)
    
    assert abs(calculated_escape_velocity - expected_escape_velocity) < 1, \
        f"Expected {expected_escape_velocity} m/s, got {calculated_escape_velocity} m/s"
