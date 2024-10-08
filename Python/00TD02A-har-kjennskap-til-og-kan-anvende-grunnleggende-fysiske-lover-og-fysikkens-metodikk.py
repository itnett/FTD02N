python
import matplotlib.pyplot as plt
import numpy as np

# 1. Newton's Second Law: Force, Mass, and Acceleration
F = 10  # Force (Newtons)
m = 2   # Mass (kilograms)
a = F / m  # Acceleration (m/s^2)

t = np.linspace(0, 5, 100)  # Time (seconds)
v = a * t                # Velocity (m/s)
x = 0.5 * a * t**2       # Displacement (meters)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, v)
plt.title('Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t, x)
plt.title('Displacement vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)

plt.suptitle("Newton's Second Law")
plt.show()

# 2. Thermodynamics: Heat Transfer
T1 = 80  # Initial temperature of object 1 (°C)
T2 = 20  # Initial temperature of object 2 (°C)
k = 0.5  # Thermal conductivity (W/mK)
A = 0.1  # Contact area (m^2)
d = 0.01 # Thickness (m)

t = np.linspace(0, 60, 100)  # Time (seconds)

# Calculate temperature change over time (simplified model)
T1_over_time = T1 - (T1 - T2) * np.exp(-k * A * t / (d * 1000))  
T2_over_time = T2 + (T1 - T2) * np.exp(-k * A * t / (d * 1000))

plt.figure(figsize=(10, 6))
plt.plot(t, T1_over_time, label='Object 1')
plt.plot(t, T2_over_time, label='Object 2')
plt.title('Heat Transfer Between Two Objects')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

# 3. Electromagnetism: Faraday's Law (Simplified)
t = np.linspace(0, 2 * np.pi, 100)
B = np.sin(t)  # Changing magnetic field
emf = -np.gradient(B)  # Induced electromotive force (derivative of B)

plt.figure(figsize=(10, 6))
plt.plot(t, B, label='Magnetic Field (B)')
plt.plot(t, emf, label='Induced EMF')
plt.title("Faraday's Law (Simplified)")
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
plt.show()