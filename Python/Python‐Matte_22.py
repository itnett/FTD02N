python
def kinetic_potential_energy(mass_kg=2, height_m=10, velocity_m_s=5):
    """
    Calculate kinetic and potential energy.
    
    Parameters:
    mass_kg (float): Mass in kilograms.
    height_m (float): Height in meters.
    velocity_m_s (float): Velocity in meters per second.
    
    Returns:
    tuple: Kinetic energy in joules, potential energy in joules.
    """
    g = 9.81  # acceleration due to gravity in m/s^2
    kinetic_energy = 0.5 * mass_kg * velocity_m_s**2
    potential_energy = mass_kg * g * height_m
    
    print(f"Kinetisk energi: {kinetic_energy} J")
    print(f"Potensiell energi: {potential_energy} J")
    
    return kinetic_energy, potential_energy

# Example usage
kinetic_potential_energy()