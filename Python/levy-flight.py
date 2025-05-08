import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_steps = 1000  # Number of steps
alpha = 1.5     # Lévy exponent (1 < alpha <= 2)
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

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Lévy flight path
ax1.plot(x, y, 'b-', alpha=0.5, label='Lévy Flight Path')
ax1.scatter(x, y, c='red', s=10, label='Steps')
ax1.scatter(x[0], y[0], c='green', s=100, label='Start')
ax1.scatter(x[-1], y[-1], c='blue', s=100, label='End')
ax1.set_title('2D Lévy Flight Path')
ax1.set_xlabel('X Position')
ax1.set_ylabel('Y Position')
ax1.legend()
ax1.grid(True)
ax1.axis('equal')

# Plot 2: Step length distribution (histogram)
ax2.hist(steps, bins=50, log=True, color='purple', alpha=0.7)
ax2.set_title('Step Length Distribution')
ax2.set_xlabel('Step Length')
ax2.set_ylabel('Frequency (Log Scale)')
ax2.grid(True, alpha=0.3)

# Adjust layout and save
plt.tight_layout()
plt.savefig('levy_flight_with_distribution.png')
