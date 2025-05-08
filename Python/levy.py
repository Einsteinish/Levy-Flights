import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_steps = 1000  # Number of steps in the walk
alpha = 1.5     # Lévy exponent (1 < alpha <= 2 for stable Lévy flights)
scale = 1.0     # Scaling factor for step lengths

# Initialize position
x, y = np.zeros(n_steps), np.zeros(n_steps)
x[0], y[0] = 0, 0  # Start at origin

# Generate random angles for direction
theta = np.random.uniform(0, 2 * np.pi, n_steps)

# Generate step lengths from a power-law distribution
steps = np.random.pareto(alpha, n_steps) * scale

# Compute new positions
for i in range(1, n_steps):
    x[i] = x[i-1] + steps[i] * np.cos(theta[i])
    y[i] = y[i-1] + steps[i] * np.sin(theta[i])

# Plot the Lévy flight
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-', alpha=0.5, label='Lévy Flight Path')
plt.scatter(x, y, c='red', s=10, label='Steps')
plt.scatter(x[0], y[0], c='green', s=100, label='Start')
plt.scatter(x[-1], y[-1], c='blue', s=100, label='End')
plt.title('2D Lévy Flight Simulation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.grid(True)
plt.savefig('levy_flight.png')
