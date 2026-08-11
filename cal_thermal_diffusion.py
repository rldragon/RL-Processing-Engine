import numpy as np

# Calculates 1D temperature diffusion and returns the temperature profile at the target_time.
def cal_temperature_1d(length, T_arr, num_steps, alpha, target_time, Lboundary: bool, Rboundary: bool):

    time_step = target_time / num_steps

    # Calculate grid spacing and time step
    dx = length / (len(T_arr) - 1)
    dt = time_step
    cfl = alpha * dt / (dx ** 2)
    
    # Input validation and safety checks
    if cfl >= 0.5:
        raise ValueError(f"Simulation unstable (CFL = {cfl:.3f} >= 0.5). Decrease dt or increase dx.")

    T_left,T_right = None,None
    if Lboundary:
        T_left = T_arr[0]
    if Rboundary:
        T_right = T_arr[-1]

    T_next = T_arr.copy()
    T = T_arr # use a shorter variable
    T_arr = None # variable unused reassign to none

    # Run the loop up to the requested target time
    for _ in range(num_steps):
        # Finite difference update for internal nodes
        T_next[1:-1] = T[1:-1] + cfl * (T[2:] - 2 * T[1:-1] + T[:-2])

        if Lboundary:
            T[0] = T_left
        if Rboundary:
            T[-1] = T_right

        T = T_next.copy()
        
    return T