import numpy as np
from cal_thermal_diffusion import cal_temperature_1d


sim_length = 1 # in meters
T_start = 25 # in celsius
T_insert_left = 120
resolution = 10
time = 1 # in seconds
time_res = 10000
thermal_conductivity = 0.025 # of air

T_arr = np.array([float(T_start)] * resolution) # create temperature array
T_arr[0] = float(T_insert_left) # left
print(T_arr)

T_arr = cal_temperature_1d(
    length=sim_length, 
    T_arr=T_arr, 
    num_steps=time_res, 
    alpha=thermal_conductivity, 
    target_time=time,
    Lboundary=True,
    Rboundary=False
)

print(np.round(T_arr, 2))
print(f"t = {time} seconds:")

def main():
    pass