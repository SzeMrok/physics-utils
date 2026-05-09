import pint
import math

_si = pint.UnitRegistry()

# gravitational constant
G = 6.67430e-11 * _si.meter**3 / (_si.kilogram * _si.second**2)


def escape_velocity(M: float, R: float) -> float:
    """
    Calculate the escape velocity.
    
    Args:
        M (float): Mass of the celestial body (in kilograms).
        R (float): Radius from the center of the celestial body (in meters).
    
    Returns:
    float: Escape velocity (in meters per second).
    """
    
    if not isinstance(M, _si.Quantity):
        M = M * _si.kg
        
    if not isinstance(R, _si.Quantity):
        R = R * _si.m
        
    return (2 * G * M / R) ** 0.5


def orbital_velocity(M: float, R: float) -> float:
    """
    Calculate the orbital velocity.
    
    Args:
        M (float): Mass of the celestial body (in kilograms).
        R (float): Radius from the center of the celestial body (in meters).
    
    Returns:
        float: Orbital velocity (in meters per second).
    """
    
    if not isinstance(M, _si.Quantity):
        M = M * _si.kg
        
    if not isinstance(R, _si.Quantity):
        R = R * _si.m
        
    return (G * M / R) ** 0.5


def orbital_period(M: float, a: float) -> float:
    """
    Calculate the orbital period.
    
    Args:
        M (float): Mass of the celestial body (in kilograms).
        a (float): Semi-major axis of the orbit (in meters).
    
    Returns:
        float: Orbital period (in seconds).
    """
    
    if not isinstance(M, _si.Quantity):
        M = M * _si.kg
        
    if not isinstance(a, _si.Quantity):
        a = a * _si.m
        
    return 2 * math.pi * (a**3 / (G * M)) ** 0.5
