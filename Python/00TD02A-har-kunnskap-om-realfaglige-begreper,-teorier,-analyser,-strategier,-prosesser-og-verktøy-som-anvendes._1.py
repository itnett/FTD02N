python
import math

# Password parameters
length = 12
num_characters = 95  # Assuming 95 printable ASCII characters

# Calculate possible combinations
combinations = num_characters**length

# Estimate time to crack (simplified)
attempts_per_second = 1e9  # 1 billion attempts per second
time_to_crack = combinations / attempts_per_second

print(f"Possible combinations: {combinations:.2e}")
print(f"Estimated time to crack: {time_to_crack:.2e} seconds")