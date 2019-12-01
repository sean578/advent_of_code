import numpy as np


def fuel_calc(module_array):
    return (module_array // 3) - 2


module_masses = np.loadtxt('day_1.txt', dtype=np.int32)
total_fuel = np.zeros_like(module_masses)  # Hold the total fuel required for each module

fuel = fuel_calc(module_masses)  # Initial calculation of fuel for the module mass
total_fuel = total_fuel + fuel

# Loop through to calculate the total fuel required...
done = False
while not done:
    fuel = fuel_calc(fuel)

    indicies_below_zero = fuel < 0
    fuel[indicies_below_zero] = 0  # Set fuels below zero to zero

    total_fuel = total_fuel + fuel
    done = not np.all(fuel >0)  # If all new fuel calcs are zero we are done

print(np.sum(total_fuel))

