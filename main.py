import numpy as np
from cal_thermal_diffusion import cal_temperature_1d

np.set_printoptions(suppress=True, formatter={'float': '{:0.3f}'.format})

sim_length = 1 # in meters
resolution = 10 # point resolution, each point is the average of 0.1

T_start = 25 # in celsius
T_insert_left = 30 # inserting a heat source on the left

time = 1 # total simulation time
total_time = 30
time_res = 10000 # total steps in that time

thermal_diffusivity= 0.0000219 # of air (not thermla conductivity)

T_arr = np.array([float(T_start)] * resolution) # create temperature array
T_arr[0] = float(T_insert_left) # left
print(f"t: 0s{np.round(T_arr, 3)}")

for i in range(total_time):
    T_arr = cal_temperature_1d(
        length=sim_length, 
        T=T_arr, 
        num_steps=time_res, 
        alpha=thermal_diffusivity, 
        target_time=time,
        T_ambient=25, # outside air temp
        rho=1.2, # Density (kg/m^3)
        cp=1005.0, # Specific heat capacity (J/kg·K)
    )
    print(f"t: {i+1}s{np.round(T_arr, 3)}")

print('='*70)
print(f"t: {i}s{np.round(T_arr, 3)}")
print(f"t = {time} seconds")

def main():
    pass