python
def energy_conservation(mass_kg=2, height_m=10, velocity_m_s=5):
    """
    Demonstrate the principle of energy conservation.
    
    Parameters:
    mass_kg (float): Mass in kilograms.
    height_m (float): Height in meters.
    velocity_m_s (float): Velocity in meters per second.
    
    Returns:
    float: Total mechanical energy in joules.
    """
    kinetic_energy, potential_energy = kinetic_potential_energy(mass_kg, height_m, velocity_m_s)
    total_energy = kinetic_energy + potential_energy
    
    print(f"Total mekanisk energi (kinetisk + potensiell): {total_energy} J")
    return total_energy

def first_law_of_thermodynamics(internal_energy_change=500, heat_added=300):
    """
    Apply the first law of thermodynamics.
    
    Parameters:
    internal_energy_change (float): Change in internal energy in joules.
    heat_added (float): Heat added in joules.
    
    Returns:
    float: Work done in joules.
    """
    work_done = heat_added - internal_energy_change
    
    print(f"I henhold til termodynamikkens første lov, med endring i indre energi {internal_energy_change} J og tilført varme {heat_added} J, er utført arbeid {work_done} J")
    return work_done

# Example usage
energy_conservation()
first_law_of_thermodynamics()