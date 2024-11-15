import numpy as np

# Constants
G = 9.81  # Gravity (m/s^2)
RHO_0 = 1.225  # Air density at sea level (kg/m^3)

def simulate_rocket(thrust, mass, drag_coeff, area, burn_rate, time_step=0.1, max_time=300):
    # Initial conditions
    altitude, velocity = 0, 0
    fuel_mass = mass['fuel']
    rocket_mass = mass['rocket'] + mass['payload'] + fuel_mass
    
    results = {'time': [], 'altitude': [], 'velocity': []}
    
    for t in np.arange(0, max_time, time_step):
        if fuel_mass > 0:
            current_thrust = thrust
            fuel_mass -= burn_rate * time_step
        else:
            current_thrust = 0  # No thrust when fuel is gone
        
        # Air density based on altitude
        rho = RHO_0 * np.exp(-altitude / 8000)  # Simplified model
        drag_force = 0.5 * rho * velocity**2 * drag_coeff * area
        gravity_force = rocket_mass * G
        net_force = current_thrust - (drag_force + gravity_force)
        
        acceleration = net_force / rocket_mass
        velocity += acceleration * time_step
        altitude += velocity * time_step
        
        # Update rocket mass
        rocket_mass = mass['rocket'] + mass['payload'] + fuel_mass
        
        # Store results
        results['time'].append(t)
        results['altitude'].append(altitude)
        results['velocity'].append(velocity)
        
        if altitude <= 0 and t > 0:
            break  # Rocket hits the ground
    
    return results
