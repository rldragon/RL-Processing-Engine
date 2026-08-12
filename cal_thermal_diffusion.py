import numpy as np

# Calculates 1D temperature diffusion and returns the temperature profile at the target_time.
def cal_temperature_1d(length, T, num_steps, alpha, target_time, T_ambient, rho, cp):

    time_step = target_time / num_steps

    # Calculate grid spacing and time step
    dx = length/ (len(T) - 1)
    dt = time_step
    cfl = alpha * dt / (dx ** 2)
    
    # Input validation and safety checks
    if cfl >= 0.5:
        raise ValueError(f"Simulation unstable (CFL = {cfl:.3f} >= 0.5). Decrease dt or increase dx.")

    T_next = T.copy()

    # Change h to adjust the insulation quality:
    # h > 0 : Imperfectly insulated (loses heat to air)
    # h = 0 : Perfectly insulated (zero heat loss)
    h = 0   
    # k (thermal conductivity) = alpha * rho * cp
    leak_factor = (dx * h) / (alpha * rho * cp)

    # Run the loop up to the requested target time
    for _ in range(num_steps):
        # Dynamically add external ghost nodes using 'edge' padding (mimics perfect insulation)
        T_padded = np.pad(T, pad_width=1, mode='edge')

        # Finite difference update for internal nodes
        # T_next[1:-1] = T[1:-1] + cfl * (T[2:] - 2 * T[1:-1] + T[:-2])
        T_next = T + cfl * (T_padded[2:] - 2 * T + T_padded[:-2])

        # Apply the heat leak adjustment to the edges (multiplied by 2 * cfl due to central difference)
        # Note: If h = 0, leak_factor = 0, and these adjustments automatically vanish!
        T_next[0]  -= 2 * cfl * leak_factor * (T[0] - T_ambient)
        T_next[-1] -= 2 * cfl * leak_factor * (T[-1] - T_ambient)

        T = T_next.copy()

    return T