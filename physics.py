import numpy as np

def simulate_trajectory(weight, thrust, angle, time_step=0.1, max_time=120):
    g = 9.81  # Gravity (m/s^2)
    angle_rad = np.radians(angle)  # Convert angle to radians

    # Initialize values
    velocity = 0
    x, y = 0, 0
    trajectory = []

    for t in np.arange(0, max_time, time_step):
        # Forces
        thrust_force = thrust * 1000  # Convert kN to N
        acceleration = (thrust_force / weight) - g

        # Update velocity and position
        velocity += acceleration * time_step
        x += velocity * np.cos(angle_rad) * time_step
        y += velocity * np.sin(angle_rad) * time_step - 0.5 * g * time_step**2

        # Stop if rocket hits the ground
        if y <= 0:
            break

        # Save trajectory
        trajectory.append((x, y))

    return np.array(trajectory)
