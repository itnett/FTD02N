python
def physics_concepts(mass_kg=70, volume_m3=0.07):
    """
    Calculate weight and density from mass and volume.
    
    Parameters:
    mass_kg (float): Mass in kilograms.
    volume_m3 (float): Volume in cubic meters.
    
    Returns:
    tuple: Weight in newtons, density in kg/m^3.
    """
    g = 9.81  # acceleration due to gravity in m/s^2
    weight = mass_kg * g  # weight in newtons
    density = mass_kg / volume_m3  # density in kg/m^3
    
    print(f"Masse: {mass_kg} kg")
    print

(f"Tyngde: {weight} N")
    print(f"Massetetthet: {density} kg/m^3")
    
    return weight, density

# Example usage
physics_concepts()