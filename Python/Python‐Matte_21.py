python
def work_power_efficiency(force_n=10, distance_m=5, time_s=2, efficiency=0.8):
    """
    Calculate work, power, and efficiency.
    
    Parameters:
    force_n (float): Force in newtons.
    distance_m (float): Distance in meters.
    time_s (float): Time in seconds.
    efficiency (float): Efficiency as a fraction.
    
    Returns:
    tuple: Work in joules, power in watts, efficient power in watts.
    """
    work = force_n * distance_m
    power = work / time_s
    efficient_power = power * efficiency
    
    print(f"Arbeid: {work} J")
    print(f"Effekt: {power} W")
    print(f"Effektiv effekt (virkningsgrad {efficiency*100}%): {efficient_power} W")
    
    return work, power, efficient_power

# Example usage
work_power_efficiency()