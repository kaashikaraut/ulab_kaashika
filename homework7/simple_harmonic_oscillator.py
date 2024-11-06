import numpy as np
import matplotlib.pyplot as plt

#constants for SHO
mass = 1.0  # mass (kg)
k = 1.0  # spring constant (N/m)
initial_position = 1.0  #(m)
initial_velocity = 0.0  #(m/s)
time_step = 0.01  # timestep for numerical integration (s)
total_time = 10  #(s)

def simulate_oscillator(mass, k, initial_position, initial_velocity, time_step, total_time):
    """
    Simulates the motion of a simple harmonic oscillator usingthe Euler integration method.
    
    Inputs:
    mass (float): object mass (kg)
    k (float): spring constant (N/m)
    initial_position (float): initial displacement (m)
    initial_velocity (float): initial velocity (m/s)
    time_step (float): time step for integration (s)
    total_time (float): total simulation time (s)
    
    Outputs:
    positions (numpy.ndarray): positions at each time step
    velocities (numpy.ndarray): velocities at each time step
    times (numpy.ndarray): time steps
    """
    num_steps = int(total_time / time_step)
    positions = np.zeros(num_steps)
    velocities = np.zeros(num_steps)
    times = np.zeros(num_steps)
    
    #initial conditions
    positions[0] = initial_position
    velocities[0] = initial_velocity

    #numerical integration using the Euler method (I learned about this in Physics 77)
    for t in range(1, num_steps):
        times[t] = t * time_step
        acceleration = -k / mass * positions[t-1]  #hooke's law
        velocities[t] = velocities[t-1] + acceleration*time_step
        positions[t] = positions[t-1] + velocities[t-1]*time_step
    
    return positions, velocities, times

def check_harmonic_behavior(positions, threshold=0.05):
    """
    Checks if it is harmonic by looking at oscillation consistency.
    
    Inputs:
    positions (numpy.ndarray):positions at each time step
    threshold (float): how much its allowed to deviate (m)
    
    Output:
    is_harmonic (bool): whether the system exhibits harmonic motion
    """
    #check if within threshold of sin oscillations
    max_disp = np.max(np.abs(positions))  #amplitude
    max_deviation = np.max(np.abs(positions - max_disp * np.sin(np.linspace(0, 2 * np.pi, len(positions)))))
    
    if max_deviation < threshold:
        return True
    else:
        return False

def visualize_motion(positions, velocities, times):
    """
    Visualizes the motion of the oscillator in both position-time and phase space (velocity vs. position).
    
    Inputs:
    positions (numpy.ndarray): Array of positions at each time step
    velocities (numpy.ndarray): Array of velocities at each time step
    times (numpy.ndarray): Array of time steps
    """
    #plot the position vs. time
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(times, positions, label='Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    
    #plot the phase space (velocity vs position)
    plt.subplot(1, 2, 2)
    plt.plot(positions, velocities, label='Phase Space')
    plt.xlabel('Position (m)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Phase Space (Position vs Velocity)')
    
    plt.tight_layout()
    plt.show()


