python
def newtons_laws(force_n=10, mass_kg=2):
    """
    Calculate acceleration using Newton's second law.
    
    Parameters:
    force_n (float): Force in newtons.
    mass_kg (float): Mass in kilograms.
    
    Returns:
    float: Acceleration in m/s^2.
    """
    acceleration = force_n / mass_kg
    print(f"Med kraft {force_n} N og masse {mass_kg} kg er akselerasjonen {acceleration} m/s^2")
    return acceleration

def motion_equations(v0=0, a=9.81, t=1):
    """
    Calculate the position and velocity using motion equations for constant acceleration.
    
    Parameters:
    v0 (float): Initial velocity in m/s.
    a (float): Acceleration in m/s^2.
    t (float): Time in seconds.
    
    Returns:
    tuple: Final position in meters, final velocity in m/s.
    """
    v = v0 + a * t
    s = v0 * t + 0.5 * a * t**2
    
    print(f"Med initial hastighet {v0} m/s, akselerasjon {a} m/s^2 og tid {t} s er sluttposisjonen {s} m og sluthastigheten {v} m/s")
    return s, v

# Example usage
newtons_laws()
motion_equations()