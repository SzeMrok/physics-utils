from physics_utils.orbital import escape_velocity, orbital_velocity, orbital_period
from physics_utils import _si
import math


def test_escape_velocity():
    
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6  # m
    expected_escape_velocity = 11186 * _si.meter / _si.second  # m/s
    
    calculated_escape_velocity = escape_velocity(earth_mass, earth_radius)
    
    assert abs((calculated_escape_velocity - expected_escape_velocity).magnitude) < 1, \
        f"Expected {expected_escape_velocity} m/s, got {calculated_escape_velocity} m/s"
        

def test_orbital_velocity():
    
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6  # m
    expected_orbital_velocity = 7910 * _si.meter / _si.second  # m/s
    
    calculated_orbital_velocity = orbital_velocity(earth_mass, earth_radius)
    
    assert abs((calculated_orbital_velocity - expected_orbital_velocity).magnitude) < 1, \
        f"Expected {expected_orbital_velocity} m/s, got {calculated_orbital_velocity} m/s"
        

def test_orbital_period():
    
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6  # m
    expected_orbital_period = 5061 * _si.second  # s
    
    calculated_orbital_period = orbital_period(earth_mass, earth_radius)
    
    assert abs((calculated_orbital_period - expected_orbital_period).magnitude) < 1, \
        f"Expected {expected_orbital_period} s, got {calculated_orbital_period} s"
