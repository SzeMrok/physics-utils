from . import _si

def kinetic_energy(m: float, v: float) -> float:
    """
    Calculate the kinetic energy.
    
    Args:
        m (float): Mass of the object (in kilograms).
        v (float): Velocity of the object (in meters per second).
    
    Returns:
        float: Kinetic energy (in joules).
    """
    
    if not isinstance(m, _si.Quantity):
        m = m * _si.kg
        
    if not isinstance(v, _si.Quantity):
        v = v * _si.m / _si.s
        
    return 0.5 * m * v**2
