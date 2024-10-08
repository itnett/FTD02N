python
# Demonstrating SI units and prefixes in IT
#
# This script calculates and displays various quantities related to IT systems
# using appropriate SI units and prefixes.

# Data storage
data_size_bytes = 1500000000000  # 1.5 terabytes
data_size_terabytes = data_size_bytes / 1e12

# Network speed
network_speed_bps = 500000000  # 500 Mbps
network_speed_gbps = network_speed_bps / 1e9

# Processor speed
clock_speed_hz = 3400000000  # 3.4 GHz
clock_speed_ghz = clock_speed_hz / 1e9

# Output results with appropriate units and prefixes
print(f"Data size: {data_size_terabytes:.2f} TB")
print(f"Network speed: {network_speed_gbps:.2f} Gbps")
print(f"Processor speed: {clock_speed_ghz:.2f} GHz")