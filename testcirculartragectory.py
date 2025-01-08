import numpy as np
import matplotlib.pyplot as plt

R = 5
T = 10 
omega = 2 * np.pi / T
total_time = 10

# t = np.arange(0, total_time, dt)
t = np.linspace(0,total_time,20)

x = R * np.cos(omega * t)
y = R * np.sin(omega * t)

theta = np.zeros_like(t)  
for i in range(1, len(t)):
    dx = x[i] - x[i - 1]
    dy = y[i] - y[i - 1]
    theta[i] = np.arctan2(dy, dx)

plt.figure(figsize=(8, 8))
plt.plot(x, y, label="Circular Trajectory", color="blue")
plt.scatter(x[:], y[:], color="purple", label="Sample Points")

plt.title("Trajectory")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis("equal")

plt.show()
