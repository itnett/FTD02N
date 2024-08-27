python
# Demonstrating uncertainty and significant figures in IT measurements

# Measurement with uncertainty
response_time_ms = 123.5  # milliseconds
uncertainty_ms = 0.8

# Calculate relative uncertainty
relative_uncertainty_percent = (uncertainty_ms / response_time_ms) * 100

# Output results with correct significant figures
print(f"Response time: {response_time_ms:.1f} ± {uncertainty_ms:.1f} ms")
print(f"Relative uncertainty: {relative_uncertainty_percent:.1f}%")