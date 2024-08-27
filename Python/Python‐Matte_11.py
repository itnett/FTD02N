python
import math

def geometry_examples():
    # Areal og omkrets av en sirkel
    radius = 5
    area_circle = math.pi * radius**2
    circumference_circle = 2 * math.pi * radius
    print(f"Arealet av en sirkel med radius {radius} er {area_circle}")
    print(f"Omkretsen av en sirkel med radius {radius} er {circumference_circle}")
    
    # Volum og overflate av en kule
    volume_sphere = (4/3) * math.pi * radius**3
    surface_area_sphere = 4 * math.pi * radius**2
    print(f"Volumet av en kule med radius {radius} er {volume_sphere}")
    print(f"Overflaten av en kule med radius {radius} er {surface_area_sphere}")

    # GeoGebra input
    print(f"GeoGebra input for sirkel: Circle[(0, 0), {radius}]")
    print(f"GeoGebra input for kule: Sphere[(0, 0, 0), {radius}]")

geometry_examples()